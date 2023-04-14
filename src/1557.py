class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        result = set(i for i in range(n))

        for edge in edges:
            result.discard(edge[1])

        return list(result)
