# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # its just a level order where we keep the last node

        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                current = queue.popleft()

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

            result.append(current.val)

        return result

                

        