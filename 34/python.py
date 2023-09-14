class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ans = [-1,-1]
        for i in range(0,n):
            if target == nums[i]:
                ans[0] = i
                break
            if i == n - 1 and nums[i] != target:
                return ans
        for i in range(n-1, -1,-1):
            if target == nums[i]:
                ans[1] = i
                break
        return ans