class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key= lambda x: (x % 2 != 0))
        return nums