class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
            
        n = len(nums)
        l, r = 0, n - 1

        # --- Step 1: Find the Pivot (Index of the Minimum Element) ---
        while l < r:
            m = (l + r) // 2
            # If mid is greater than right, the min must be in the right half
            if nums[m] > nums[r]:
                l = m + 1
            # If mid is less/equal to right, the min is in the left half (including mid)
            else:
                r = m
        
        pivot = l  # 'l' is now the index of the smallest value
        
        # --- Step 2: Determine which subarray to search ---
        l, r = 0, n - 1
        
        # If target is in the right sorted portion (between pivot and end)
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        # Otherwise, it must be in the left sorted portion
        else:
            r = pivot - 1
            
        # --- Step 3: Standard Binary Search ---
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
                
        return -1