class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            # Skip duplicates for the fixed number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -nums[i]
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Move pointers inward
                    left += 1
                    right -= 1
                    
                    # Skip duplicates only after finding a match
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif current_sum < target:
                    # Sum too small -> Need bigger numbers -> Move left
                    left += 1
                else:
                    # Sum too big -> Need smaller numbers -> Move right
                    right -= 1
                    
        return res