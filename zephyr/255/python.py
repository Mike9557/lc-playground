class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        monotonic_stack = [preorder[0]]
        index = 1
        min_val = -1
        while index < len(preorder):
            if min_val > preorder[index]:
                return False
            if len(monotonic_stack) == 0 or monotonic_stack[-1] > preorder[index]:
                monotonic_stack.append(preorder[index])
                index += 1
            else:
                min_val = max(monotonic_stack[-1], min_val)
                monotonic_stack.pop()
        return True