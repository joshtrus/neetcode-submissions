class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None 

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.head = Node(0,0)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

        

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1 
        
        node = self.nodes[key]
        
        self._remove(node)
        self._insert_front(node)

        return node.value

        

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self._remove(self.nodes[key])
            self.nodes[key].value = value
            self._insert_front(self.nodes[key])
        else:
            node = Node(key, value)
            if len(self.nodes) < self.capacity:
                self.nodes[key] = node
                self._insert_front(node)
            else:
                del self.nodes[self.tail.prev.key]
                self._remove(self.tail.prev)
                self.nodes[key] = node
                self._insert_front(node)


        

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_front(self, node):
        temp_head = self.head.next

        temp_head.prev = node
        self.head.next = node

        node.prev = self.head
        node.next = temp_head




        
