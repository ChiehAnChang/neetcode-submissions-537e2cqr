class Solution:

    def encode(self, strs: List[str]) -> str:

        res_encode = ''

        for each_word in strs:
            res_encode = res_encode + str(len(each_word)) + '#'
            res_encode += each_word

        return res_encode


    def decode(self, s: str) -> List[str]:

        res_decode = []

        read_mode = 1
        curr_len = ''
        curr_word = ''

        for each_char in s:
            if read_mode == 1 and each_char != '#':
                curr_len += each_char

            elif read_mode == 1 and each_char == '#':
                read_mode = 0
                curr_len = int(curr_len)

                # handle empty string case: "0#"
                if curr_len == 0:
                    res_decode.append('')
                    curr_len = ''
                    curr_word = ''
                    read_mode = 1

            else:
                curr_word += each_char
                curr_len -= 1

                if curr_len == 0:
                    res_decode.append(curr_word)
                    curr_word = ''
                    curr_len = ''
                    read_mode = 1

        return res_decode