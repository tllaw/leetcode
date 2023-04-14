class Solution:
    def findCenter(self, edges):
        return list(set(edges[0]) & set(edges[1]))[0]
