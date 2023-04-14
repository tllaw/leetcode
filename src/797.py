class Solution:
    def allPathsSourceTarget(self, graph):
        result, n = [], len(graph) - 1

        def backtrack(path, i):
            if i == n:
                result.append(list(path))
                return

            for j in graph[i]:
                path.append(j)
                backtrack(path, j)
                path.pop()

        backtrack([0], 0)
        return result
