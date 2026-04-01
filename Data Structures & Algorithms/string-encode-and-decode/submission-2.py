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

            # read length until '#'
            while s[ind] != "#":
                curr_number_word_str += s[ind]
                ind += 1

            ind += 1  # skip '#'
            curr = int(curr_number_word_str)

            # read exactly `curr` characters
            each_word = ""
            for _ in range(curr):
                each_word += s[ind]
                ind += 1

            res.append(each_word)

        return res
