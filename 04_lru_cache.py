"""
LRU Cache
put and get with O(1) time complexity
"""
from typing import Optional


class Node:
    key: Optional[str]
    value: Optional[int]
    prev: Optional["Node"]
    next: Optional["Node"]

    def __init__(self, key: Optional[str], value: Optional[int]):
        self.key = key
        self.value = value


class LRUCache:
    capacity: int
    cache: dict
    head: Node
    tail: Node

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def display_dll(self) -> str:
        result = ""
        current = self.head.next
        while current != self.tail:
            result += current.key + " <-> "
            current = current.next
        result += "."
        return result

    @staticmethod
    def _remove(node: Node):
        # Remove a node
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_after_head(self, node: Node):
        # Add node to right of head
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        next_node.prev = node
        node.next = next_node

    def put(self, key: str, value: int):
        if node := self.cache.get(key):
            print("* Delete Existed Node *", key)
            self._remove(node)
            del self.cache[key]
            node.value = value
        else:
            node = Node(key, value)

        while len(self.cache) >= self.capacity:
            lru_node = self.tail.prev
            print("* Delete LRU Node *", lru_node.key)
            self._remove(lru_node)
            del self.cache[lru_node.key]

        self._insert_after_head(node)
        self.cache[key] = node

    def get(self, key: str) -> Optional[int]:
        if key not in self.cache:
            return
        node = self.cache[key]
        self._remove(node)
        self._insert_after_head(node)
        return node.value


def run_tests():
    lru_cache = LRUCache(capacity=3)
    lru_cache.put("a", 1)
    print(1, lru_cache.display_dll())
    lru_cache.put("b", 2)
    print(2, lru_cache.display_dll())
    lru_cache.put("c", 3)
    print(3, lru_cache.display_dll())
    
    c = lru_cache.get("c")
    print(4, lru_cache.display_dll())
    assert c == 3, c

    b = lru_cache.get("b")
    print(5, lru_cache.display_dll())
    assert b == 2, b

    a = lru_cache.get("a")
    print(6, lru_cache.display_dll())
    assert a == 1, a

    lru_cache.put("d", 4)
    print(7, lru_cache.display_dll())

    c = lru_cache.get("c")
    print(8, lru_cache.display_dll())
    assert c is None, c

    d = lru_cache.get("d")
    print(9, lru_cache.display_dll())
    assert d == 4, d

    lru_cache.put("e", 5)
    print(10, lru_cache.display_dll())

    assert lru_cache.get("b") is None
    assert lru_cache.get("e") == 5

    lru_cache.put("a", 101)
    print(11, lru_cache.display_dll())
    assert lru_cache.get("a") == 101
    print(12, lru_cache.display_dll())

    lru_cache.put("f", 6)
    print(13, lru_cache.display_dll())
    assert lru_cache.get("d") is None

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
