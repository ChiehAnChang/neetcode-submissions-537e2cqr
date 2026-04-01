class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(numbers)):
            num = numbers[i]
            curr = (target - num)
            if curr < num and curr in d:
                return [d[curr] + 1, i+1 ]
            # elif curr == num:
            #     return [i + 1, i + 1]
            else:
                d[num] = i
            
                
