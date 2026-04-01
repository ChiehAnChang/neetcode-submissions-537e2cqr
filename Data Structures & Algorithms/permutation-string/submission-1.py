class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length1, length2 = len(s1), len(s2)
        
        if length1 > length2:
            return False


        checklist = [0] * 26
        curr_window = [0] * 26

        for i in range(length1):

            checklist[ord(s1[i]) - ord('a')] += 1
            curr_window[ord(s2[i]) - ord('a')] += 1


        left, right = 0, length1 - 1

        while right < length2 - 1:

            if checklist == curr_window:
                return True
            else:
                curr_window[ord(s2[left]) - ord('a')] -= 1
                left += 1
                right += 1
                curr_window[ord(s2[right]) - ord('a')] += 1

        return checklist == curr_window
