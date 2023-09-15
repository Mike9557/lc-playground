class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        offset = 0
        left = 0
        right = 0
        output = collections.deque([])
        def bfs(node):
            nonlocal offset
            nonlocal left
            nonlocal right
            nonlocal output
            if node == None:
                return
            node_stack = [node]
            index_stack = [0]
            output.append([])
            while len(node_stack) != 0:
                tmp_node = node_stack[0]
                index = index_stack[0]
                if tmp_node != None:
                    while index < left:
                        output.appendleft([])
                        offset += 1
                        left -= 1    
                    while index > right:
                        output.append([])
                        right += 1
                    output[offset + index].append(tmp_node.val)
                    node_stack.append(tmp_node.left)
                    index_stack.append(index - 1)
                    node_stack.append(tmp_node.right)
                    index_stack.append(index + 1)
                node_stack.pop(0)
                index_stack.pop(0)
        bfs(root)
        return list(output)