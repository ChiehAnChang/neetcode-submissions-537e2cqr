class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        phone_book = {

            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }
        def dfs(path, curr_i):

            if curr_i == len(digits):
           
                return res.append("".join(path))

            choices_list = phone_book[int(digits[curr_i])]

            for each_choice in choices_list:

                path.append(each_choice)

                dfs(path, curr_i + 1)

                path.pop()

        dfs([], 0)
        return res

