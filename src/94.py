class Solution:
    def inorderTraversal(self, root):
        result = []
        # [node, is_left_visited]
        stack = [[root, False]]

        while stack:
            curr = stack.pop()

            if not curr[0]:
                continue

            # left node visited
            if curr[1]:
                # add current node value to `result`
                result.append(curr[0].val)
                # append right node
                stack.append([curr[0].right, False])
            # left node not visited
            else:
                # mark `is_left_visited` of current node as `True`
                stack.append([curr[0], True])
                # append left node
                stack.append([curr[0].left, False])

        return result
