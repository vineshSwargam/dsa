class Solution:
    def encode(self, strs) -> str:
        encoded_str = "".join(f'{len(s)}#{s}' for s in strs)
        # print('encoded - ', encoded_str)
        return encoded_str
        

    def decode(self, s: str):
        res = []
        i = 0
        j = 0
        collecting = False
        strs = []
        # - 5#Hello5#World
        # - 10#Superwoman8#Superman
        #  s = 14

        while i<len(s):
            j = s.index('#', i) # index of hashtag - 2
            word_len = int(s[i:j]) # 0:2 = 10
            i = word_len + j + 1  # 10 + 2 + 1
            strs.append(s[j+1:j+word_len+1])

        print('dec - ', strs)
        return strs


def test_encode_decode(strs):
    sol = Solution()
    s = sol.encode(strs)
    # print(s)
    ds = sol.decode(s)
    # print(ds)



test_encode_decode(["Hello", "World"])
test_encode_decode([""])
test_encode_decode([])