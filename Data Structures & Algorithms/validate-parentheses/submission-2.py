class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            ')': '(',
            ']': '[',
            '}':'{'
        }

        for each_bracket in s:
            if each_bracket in d:
                if len(stack) == 0:
                    return False
                elif stack.pop() != d[each_bracket]:
                    return False
            else:
                stack.append(each_bracket)
        return not stack