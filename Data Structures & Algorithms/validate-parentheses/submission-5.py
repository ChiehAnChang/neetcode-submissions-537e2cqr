class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []

        for each_c in s:
            if each_c not in d:
                if not stack:
                    return False
                end = stack[-1]
                if d[end] != each_c:
                    return False
                stack.pop()
            else:
                stack.append(each_c)
        if stack:
            return False
        return True