class Node:
    def __init__(self, key, value, next=None):
        self.key   = key
        self.value = value
        self.next  = next

class MyHashMap:
    def __init__(self):
        self.size = 19997
        self.prime = 12582917
        self.hashmap = [Node(-1, -1) for _ in range(self.size)]

    def hash(self, key):
        return key * self.prime % self.size

    def put(self, key, value):
        self.remove(key)
        head = self.hashmap[self.hash(key)]
        node = Node(key, value, head.next)
        head.next = node

    def get(self, key):
        curr = self.hashmap[self.hash(key)]

        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next

        return -1

    def remove(self, key):
        prev = self.hashmap[self.hash(key)]
        curr = prev.next

        while curr:
            if curr.key == key:
                prev.next = curr.next
                return

            prev = curr
            curr = curr.next
