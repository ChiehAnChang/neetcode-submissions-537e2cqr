class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s) - 1

        while left < right:
            left_c = s[left].lower()
            if not left_c.isalnum():
                left += 1 
                continue
            right_c = s[right].lower()
            if not right_c.isalnum():
                print(right_c)
                right -= 1 
                continue
            if left_c != right_c:
                return False
            left, right = left + 1, right - 1
        
        return True