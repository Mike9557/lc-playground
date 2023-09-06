class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)

        # If x is outside the 32-bit signed integer range
        if x > INT_MAX or x < INT_MIN:
            return 0

        if x < 0:
            s = str(x)[1:]
            y = -int(s[::-1])
        else:
            s = str(x)
            y = int(s[::-1])

        # Check if the reversed value is within 32-bit signed integer range
        if y > INT_MAX or y < INT_MIN:
            return 0

        return y






