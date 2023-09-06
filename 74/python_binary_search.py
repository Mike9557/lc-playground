class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        a = 0 
        b = m - 1
        mid = (a+b)/2

        while(a <= b):
            mid = (a+b)//2
            #)
            if(matrix[mid][0] > target):
                b = mid - 1


            
            elif(matrix[mid][n-1] < target):
                a = mid + 1
            elif ((matrix[mid][0]) <= target ) and ((matrix[mid][n-1] >= target)):
                b = -1
                a = mid
        if matrix[mid][0] > target or matrix[mid][n -1] < target:
            return False


        a = 0
        b = n -1 
        midcol = (a+b)//2

        while(a <= b):
            midcol = (a+b)//2
            if(matrix[mid][midcol]<target):
                print(0)
                a = midcol + 1

            
            elif(matrix[mid][midcol] > target):
                print(1)
                b = midcol -1
            else:
                return True
            
        print(mid,midcol)
        return False