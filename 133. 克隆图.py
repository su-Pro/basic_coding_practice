vt = {}


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        if node in vt:
            return vt[node]
        new_head = Node(node.val, [])
        vt[node] = new_head
        new_head.neighbors = [self.cloneGraph(v) for v in node.neighbors]
        return new_head
