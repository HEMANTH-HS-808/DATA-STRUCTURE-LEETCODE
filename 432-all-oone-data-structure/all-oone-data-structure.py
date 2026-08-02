class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_node = {}

    def add_after(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key):
        if key not in self.key_node:
            node = self.head
        else:
            node = self.key_node[key]
            node.keys.remove(key)

        next_node = node.next
        if next_node is self.tail or next_node.count != node.count + 1:
            next_node = Node(node.count + 1)
            self.add_after(node, next_node)

        next_node.keys.add(key)
        self.key_node[key] = next_node

        if node is not self.head and not node.keys:
            self.remove(node)

    def dec(self, key):
        node = self.key_node[key]
        node.keys.remove(key)

        if node.count == 1:
            del self.key_node[key]
        else:
            prev_node = node.prev
            if prev_node is self.head or prev_node.count != node.count - 1:
                new_node = Node(node.count - 1)
                self.add_after(node.prev, new_node)
                prev_node = new_node
            prev_node.keys.add(key)
            self.key_node[key] = prev_node

        if not node.keys:
            self.remove(node)

    def getMaxKey(self):
        return next(iter(self.tail.prev.keys)) if self.tail.prev != self.head else ""

    def getMinKey(self):
        return next(iter(self.head.next.keys)) if self.head.next != self.tail else ""