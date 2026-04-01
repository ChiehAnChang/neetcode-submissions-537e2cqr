class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]  # fix: +1 bucket

        checklist = defaultdict(int)

        for each_num in nums:  
            checklist[each_num] += 1

        for each_num in checklist:
            bucket[checklist[each_num]].append(each_num) 

        res = []
        for each_bucket_i in range(len(bucket) - 1, -1, -1): 
            each_bucket = bucket[each_bucket_i]

            for each_num in each_bucket:  
                res.append(each_num)
                if len(res) == k:  
                    return res

        return res