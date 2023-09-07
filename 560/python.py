class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0 
        n = len(nums)
        max_length = 0
        d = {0:1} 
        for i in range(0,n):
            total += nums[i]
            ##    max_length = i + 1
            
            if total - k in d : 
                max_length = max_length + d[total - k]

            if total not in d:
                d[total] = 1
            else:
                d[total] = d[total]+1

            
        

        return max_length 
                