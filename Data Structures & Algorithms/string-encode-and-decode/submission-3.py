class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for each_word in strs:
            s = s + str(len(each_word)) + "#" + each_word
        return s

    def decode(self, s: str) -> List[str]:
        ind = 0
        res = []

        while ind < len(s):
            curr_number_word_str = ""

            while s[ind] != "#":
                curr_number_word_str += s[ind]
                ind += 1
            
            ind += 1
            curr = int(curr_number_word_str)

            each_word = s[ind : ind + curr]
            ind = ind + curr

            res.append(each_word)
        
        return res
