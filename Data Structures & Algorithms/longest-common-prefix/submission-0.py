class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = ""
        stop = False
        for each_char_i in range(len(strs[0])):
            for each_word_i in range(len(strs)):
                each_word = strs[each_word_i]
                if not ((len(each_word) > each_char_i) and each_word[each_char_i] ==  strs[0][each_char_i]):
                    return prefix
            prefix += strs[0][each_char_i]
        return prefix
        