# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Count the nodes in the list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Base size and the number of longer parts
        width, extra = divmod(length, k)

        ans = []
        curr = head
        for i in range(k):
            # Create the head of this part
            part_head = curr
            # Determine the size of this part
            part_size = width + (1 if i < extra else 0)
            # Split the list for this part
            for j in range(part_size - 1):  # -1 because we already have part_head
                if curr:
                    curr = curr.next
            if curr:
                temp = curr
                curr = curr.next
                temp.next = None  # break off the list
            ans.append(part_head)

        return ans