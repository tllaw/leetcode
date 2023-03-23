class Solution:
    def levelOrder(self, root):
        queue  = [[root, 0]]
        result = []

        while queue:
            el, level = queue.pop(0)

            if not el:
                continue

            queue.extend([[el.left, level + 1], [el.right, level + 1]])

            if len(result) > level:
                result[level].append(el.val)
            else:
                result.append([el.val])

        return result
