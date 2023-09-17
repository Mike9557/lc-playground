class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        setA = set()
        setB = set()
        for node in tree:
            setA.add(node)
            for child in node.children:
                setB.add(child)
        return (setA - setB).pop()