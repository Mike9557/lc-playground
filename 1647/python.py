class Solution:
    def minDeletions(self, s: str) -> int:
        d = {}
        values = set()
        for i in s:
            if i in d.keys():
                d[i] += 1 
            else:
                d[i] = 1
        #values = set(d.values())

        def helper(value,s):
            down_value = value
            #up_value = value
            counter = 0  
            while down_value in  s and down_value != 0 :
                down_value -= 1
                counter += 1
            return counter, down_value
                
        ans = 0 
        for value in d.values():
            if value in values:
                i, new = helper(value, values)
                ans += i 
                values.add(new)
            else:
                values.add(value)
        #print(values)
        return ans

