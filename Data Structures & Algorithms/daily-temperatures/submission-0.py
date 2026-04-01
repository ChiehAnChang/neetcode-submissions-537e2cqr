class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        stack = []
        res = [0] * len(temperatures)

        for curr_i, curr_temp in enumerate(temperatures):
            while stack and stack[-1][1] < curr_temp:
                prev_i, prev_temp = stack.pop()
                res[prev_i] = curr_i - prev_i
            stack.append((curr_i, curr_temp))
        return res



                    