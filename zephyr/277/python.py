class Solution:
    def findCelebrity(self, n: int) -> int:
        ans = 0
        for i in range(1, n):
            if knows(ans, i):
                ans = i
        
        for i in range(ans):
            if knows(ans, i):
                return -1

        for i in range(n):
            if not knows(i, ans):
                return -1
        return ans