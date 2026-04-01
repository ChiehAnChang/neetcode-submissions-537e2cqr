class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # FIX 1: "l < r" prevents the loop from running if there is only 1 item.
        # If nums = [1], l=0, r=0. The loop is skipped.
        while l < r:
            m = (l + r) // 2

            # LOGIC SAFETY:
            # Since l < r, math guarantees that 'm' is strictly less than 'r'.
            # Therefore, 'm + 1' will always be a valid index <= r.
            
            # Rule 1: Both sides normal
            if nums[l] <= nums[m] and nums[m + 1] <= nums[r]:
                if nums[l] < nums[m + 1]:
                    return nums[l]
                else:
                    return nums[m + 1]

            # Rule 2: Left side normal, abnormal is on right
            elif nums[l] <= nums[m]:
                l = m + 1
            
            # Rule 2: Left side abnormal, min is on left
            else:
                r = m 

        # FIX 2: If the loop is skipped (1 item) or finishes, return the single remaining item.
        return nums[l]