class Solution:
    def canVisitAllRooms(self, rooms):
        stack, result = [0], [False for _ in range(len(rooms))]

        while stack:
            room = stack.pop()

            if result[room]:
                continue

            result[room] = True
            stack.extend(rooms[room])

        for i in result:
            if not i:
                return False

        return True
