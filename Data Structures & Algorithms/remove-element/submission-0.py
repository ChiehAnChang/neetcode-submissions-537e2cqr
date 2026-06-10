class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        left, right = 0, len(nums) - 1

        if len(nums) == 0 or (len(nums) == 1 and nums[0] == val):
            return 0
        else:
            while left < right:
                if nums[left] != val:
                    left += 1
                    continue
                else:
                    nums[left], nums[right] = nums[right], nums[left]
                    right -= 1
                
            if nums[left] == val:
                return left
            else:
                return left + 1