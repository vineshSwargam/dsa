#!/usr/bin/env python3
"""Scaffold a NeetCode problem into this repo.

Usage (run from the folder where the new file should live):

    cd linked_list
    ../venv/bin/python ../new_problem.py https://neetcode.io/problems/<slug>/question

Flags:
    --no-git   only scrape and write the file, skip branch/commit/push
    --headed   show the browser window while scraping (debugging)

What it does:
    1. Opens the page, makes sure the Question tab is active, expands the
       collapsed Topics / Hints / Company Tags sections.
    2. Copies the whole left panel as comments and the Python starter code
       from the right panel verbatim.
    3. Adds `sol = Solution()`, the examples as variable assignments (first
       one live, the rest commented out) and a call to the solution method.
    4. Writes <snake_case_title>.py into the current directory.
    5. git checkout -b <kebab-case-title>, commit "init", push -u origin.
    6. Opens a pull request titled after the branch ("subtree-of-another-tree"
       becomes "Subtree of another tree") with the problem URL as the body.
       Uses the GitHub REST API with the token in $DSA_GITHUB_TOKEN; without a
       token it opens the prefilled "compare" page in your browser instead so
       you only have to click "Create pull request". Never uses the gh CLI.

One-time setup:
    venv/bin/pip install playwright
    venv/bin/playwright install chromium
    # optional, for automatic PR creation: a fine-grained personal access token
    # on the *personal* GitHub account with "Pull requests: read and write" on
    # this repo, exported as DSA_GITHUB_TOKEN in your shell profile.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from pathlib import Path

try:
    from playwright.sync_api import TimeoutError as PlaywrightTimeout
    from playwright.sync_api import sync_playwright
except ImportError:
    # Re-run under the repo's venv (which has playwright) if we're not in it yet.
    venv_dir = Path(__file__).resolve().parent / "venv"
    venv_python = venv_dir / "bin" / "python"
    in_venv = Path(sys.prefix).resolve() == venv_dir.resolve()
    if venv_python.exists() and not in_venv and not os.environ.get("NEW_PROBLEM_REEXEC"):
        os.environ["NEW_PROBLEM_REEXEC"] = "1"
        os.execv(str(venv_python), [str(venv_python), __file__, *sys.argv[1:]])
    sys.exit(
        "playwright is not installed. Run:\n"
        "  venv/bin/pip install playwright && venv/bin/playwright install chromium"
    )

# Monaco only renders the lines that are on screen, so the viewport is made
# very tall and wide (see scrape()) and the rendered rows are read back in
# order. A long line that Monaco soft-wraps becomes several rows; the gutter
# shows a line number only on the first row, so rows without one are glued
# back onto the previous row.
JS_READ_EDITOR = """
() => {
  const editors = [...document.querySelectorAll('.monaco-editor')];
  if (!editors.length) return '';
  const editor = editors.reduce((best, e) =>
    e.querySelectorAll('.view-line').length > best.querySelectorAll('.view-line').length ? e : best);

  const numbered = new Set(
    [...editor.querySelectorAll('.margin-view-overlays > div')]
      .filter(d => (d.querySelector('.line-numbers')?.textContent || '').trim() !== '')
      .map(d => parseInt(d.style.top, 10)));

  const rows = [...editor.querySelectorAll('.view-lines .view-line')]
    .map(l => ({ top: parseInt(l.style.top, 10), text: l.textContent.replace(/\\u00a0/g, ' ') }))
    .sort((a, b) => a.top - b.top);

  const lines = [];
  for (const row of rows) {
    if (numbered.has(row.top) || lines.length === 0) lines.push(row.text);
    else lines[lines.length - 1] += row.text.replace(/^\\s+/, '');
  }
  return lines.map(l => l.replace(/\\s+$/, '')).join('\\n');
}
"""


# --------------------------------------------------------------------------- #
# Scraping
# --------------------------------------------------------------------------- #
def scrape(url: str, headed: bool = False):
    """Return (title, left_panel_text, python_starter_code)."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headed)
        page = browser.new_page(viewport={"width": 2400, "height": 4000})
        page.goto(url, wait_until="domcontentloaded")
        page.wait_for_selector("h1.problem-title", timeout=30_000)

        # 1. Make sure the Question tab is the active one in the left panel.
        active = page.locator("ul.tabs-list li.my-active-tab").first
        if active.count() == 0 or active.inner_text().strip() != "Question":
            page.locator("ul.tabs-list a[href$='/question']").first.click()
        page.wait_for_selector(".question-tab", timeout=15_000)

        # 2. Expand Topics / Recommended complexity / Hints / Company Tags so
        #    their bodies are part of the copied text. The bodies are only
        #    rendered on a real click, so click every collapsed summary.
        summaries = page.locator(".question-tab details:not([open]) > summary")
        for i in range(summaries.count()):
            summaries.nth(0).click()
            page.wait_for_timeout(150)
        page.wait_for_timeout(500)

        title = page.locator("h1.problem-title").first.inner_text().strip()
        left = page.locator(".question-tab").first.inner_text()

        # 3. Make sure the editor language is Python.
        lang_btn = page.locator("button.editor-language-btn")
        page.wait_for_selector("button.editor-language-btn", timeout=15_000)
        current = lang_btn.locator(".selected-language").inner_text().strip()
        if current != "Python":
            lang_btn.click()
            page.locator("a.dropdown-item", has_text=re.compile(r"^\s*Python\s*$")).first.click()
            page.wait_for_timeout(800)

        # 4. Read the starter code once it has finished loading (poll until
        #    the editor text is non-empty and stable).
        code = _wait_for_stable_editor(page)
        browser.close()

    return title, left, code


def _wait_for_stable_editor(page, attempts: int = 40, interval_ms: int = 250) -> str:
    previous = None
    for _ in range(attempts):
        current = page.evaluate(JS_READ_EDITOR)
        if current.strip() and current == previous:
            return current
        previous = current
        page.wait_for_timeout(interval_ms)
    if previous and previous.strip():
        return previous
    raise PlaywrightTimeout("Editor never showed any code. Is the URL a NeetCode problem page?")


# --------------------------------------------------------------------------- #
# Text processing
# --------------------------------------------------------------------------- #
def kebab(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def snake(title: str) -> str:
    return kebab(title).replace("-", "_")


def camel_to_snake(name: str) -> str:
    """addTwoNumbers -> add_two_numbers, getMin -> get_min, parseURLPath -> parse_url_path."""
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    return name.lower()


def snake_case_methods(code: str) -> str:
    """Rename every non-dunder `def camelCase(` in the starter code to snake_case."""
    def repl(m):
        name = m.group(2)
        if name.startswith("__"):
            return m.group(0)
        return f"{m.group(1)}{camel_to_snake(name)}{m.group(3)}"
    return re.sub(r"^(\s*def\s+)(\w+)(\s*\()", repl, code, flags=re.MULTILINE)


def comment_block(text: str) -> str:
    out = []
    for line in text.splitlines():
        line = line.rstrip()
        out.append(f"# {line}" if line.strip() else "")
    return "\n".join(out)


def find_class_and_method(code: str):
    """Return (class_name, method_name) from the starter code, ignoring commented lines."""
    classes = list(re.finditer(r"^class\s+(\w+)", code, re.MULTILINE))
    if not classes:
        return None, None
    cls = classes[-1]  # Solution is always the last real class in the stub
    body = code[cls.end():]
    for m in re.finditer(r"^\s+def\s+(\w+)\s*\(\s*self", body, re.MULTILINE):
        if not m.group(1).startswith("__"):
            return cls.group(1), m.group(1)
    return cls.group(1), None


def split_top_level(s: str, sep: str = ",") -> list:
    """Split on `sep` but not inside brackets or quotes."""
    parts, depth, quote, buf = [], 0, None, []
    for ch in s:
        if quote:
            buf.append(ch)
            if ch == quote:
                quote = None
            continue
        if ch in "\"'":
            quote = ch
        elif ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        if ch == sep and depth == 0:
            parts.append("".join(buf).strip())
            buf = []
        else:
            buf.append(ch)
    if buf:
        parts.append("".join(buf).strip())
    return [p for p in parts if p]


def parse_examples(left: str) -> list:
    """Return [(names, values, output_text), ...] for every Example block."""
    examples = []
    pattern = re.compile(r"Input:\s*(.+?)\n\s*\n?\s*Output:\s*(.+?)(?:\n|$)", re.DOTALL)
    for m in pattern.finditer(left):
        raw_input, raw_output = m.group(1).strip(), m.group(2).strip()
        names, values = [], []
        for assignment in split_top_level(raw_input):
            if "=" not in assignment:
                continue
            name, value = assignment.split("=", 1)
            names.append(name.strip())
            values.append(value.strip())
        if names:
            examples.append((names, values, raw_output))
    return examples


def build_file(title: str, left: str, code: str) -> str:
    gap = "\n\n\n"
    code = snake_case_methods(code)
    sections = [comment_block(left), code.rstrip()]

    class_name, method_name = find_class_and_method(code)
    examples = parse_examples(left)

    tail = []
    if class_name:
        var = class_name.lower()[:3]
        tail.append(f"{var} = {class_name}()")
        for i, (names, values, output) in enumerate(examples):
            line = f"{', '.join(names)} = {', '.join(values)} # Output {output}"
            tail.append(line if i == 0 else f"# {line}")
        if method_name:
            args = ", ".join(examples[0][0]) if examples else ""
            tail.append(gap + f"print({var}.{method_name}({args}))")
    if tail:
        sections.append("\n".join(tail))

    return gap.join(sections) + "\n"


# --------------------------------------------------------------------------- #
# Git
# --------------------------------------------------------------------------- #
def run(cmd: list, cwd: Path):
    print("$", " ".join(cmd))
    result = subprocess.run(cmd, cwd=cwd)
    if result.returncode != 0:
        sys.exit(f"'{' '.join(cmd)}' failed with exit code {result.returncode}, stopping.")


def commit_and_push(branch: str, file_path: Path):
    cwd = file_path.parent
    run(["git", "add", str(file_path)], cwd)
    run(["git", "commit", "-m", "init"], cwd)
    run(["git", "push", "-u", "origin", branch], cwd)


# --------------------------------------------------------------------------- #
# Pull request
# --------------------------------------------------------------------------- #
TOKEN_ENV = "DSA_GITHUB_TOKEN"
BASE_BRANCH = "main"


def pr_title(branch: str) -> str:
    """subtree-of-another-tree -> Subtree of another tree"""
    return branch.replace("-", " ").capitalize()


def repo_slug(cwd: Path) -> str:
    """owner/repo parsed from the origin URL (ssh alias or https)."""
    url = subprocess.run(
        ["git", "remote", "get-url", "origin"], cwd=cwd, capture_output=True, text=True, check=True
    ).stdout.strip()
    m = re.search(r"[:/]([^/:]+/[^/]+?)(?:\.git)?/?$", url)
    if not m:
        sys.exit(f"Could not work out owner/repo from origin url '{url}'.")
    return m.group(1)


def compare_url(slug: str, branch: str, title: str, body: str) -> str:
    query = urllib.parse.urlencode({"expand": "1", "title": title, "body": body})
    return f"https://github.com/{slug}/compare/{BASE_BRANCH}...{branch}?{query}"


def create_pull_request(branch: str, body: str, cwd: Path):
    slug = repo_slug(cwd)
    title = pr_title(branch)
    token = os.environ.get(TOKEN_ENV)

    if token:
        req = urllib.request.Request(
            f"https://api.github.com/repos/{slug}/pulls",
            data=json.dumps({"title": title, "head": branch, "base": BASE_BRANCH, "body": body}).encode(),
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github+json",
                "Content-Type": "application/json",
                "User-Agent": "new_problem.py",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                pr = json.load(resp)
            print(f"PR created: {pr['html_url']}")
            return
        except urllib.error.HTTPError as e:
            detail = e.read().decode(errors="replace")
            print(f"GitHub API refused the PR ({e.code}): {detail[:300]}")
        except urllib.error.URLError as e:
            print(f"Could not reach the GitHub API: {e.reason}")
        print("Falling back to the compare page.")
    else:
        print(f"{TOKEN_ENV} is not set, so opening the prefilled compare page instead.")

    url = compare_url(slug, branch, title, body)
    print(f"Create the PR here: {url}")
    webbrowser.open(url)


# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url", help="NeetCode problem URL")
    ap.add_argument("--no-git", action="store_true", help="skip branch / commit / push")
    ap.add_argument("--headed", action="store_true", help="show the browser while scraping")
    args = ap.parse_args()

    print(f"Scraping {args.url} ...")
    title, left, code = scrape(args.url, headed=args.headed)
    print(f"Title: {title}")

    branch = kebab(title)
    file_path = Path.cwd() / f"{snake(title)}.py"
    if file_path.exists():
        sys.exit(f"{file_path} already exists, refusing to overwrite.")

    # Branch first so an already-existing branch fails before anything is written.
    if not args.no_git:
        run(["git", "checkout", "-b", branch], file_path.parent)

    file_path.write_text(build_file(title, left, code))
    print(f"Wrote {file_path}")

    if args.no_git:
        print("Skipping git (--no-git).")
        return

    commit_and_push(branch, file_path)
    print(f"Branch '{branch}' pushed.")
    create_pull_request(branch, body=args.url, cwd=file_path.parent)


if __name__ == "__main__":
    main()
