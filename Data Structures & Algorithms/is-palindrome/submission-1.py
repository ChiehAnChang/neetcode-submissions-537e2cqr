class Solution:
    def isPalindrome(self, s: str) -> bool:
        left,right = 0, len(s) - 1

        while left < right:
            # check if the char is alphanumeric
            left_char, right_char = s[left], s[right]
            if not left_char.isalnum():
                left += 1
                continue
            if not right_char.isalnum():
                right -= 1
                continue
            if left_char.lower() != right_char.lower():
                return False
            left, right = left + 1, right - 1
        return True
        