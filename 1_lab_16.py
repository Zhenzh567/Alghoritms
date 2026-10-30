import random

class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def remove(self, key):
        current = self.head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                return
            current = current.next

    def sort(self, key=None, reverse=False):
        if not self.head or not self.head.next:
            return
        sorted_list = None
        current = self.head
        while current is not None:
            next_node = current.next
            sorted_list = self._sorted_insert(sorted_list, current, key, reverse)
            current = next_node
        self.head = sorted_list

    def _sorted_insert(self, head_ref, new_node, key, reverse):
        new_node.prev = None
        new_node.next = None
        val_new = key(new_node.data) if key else new_node.data
        if head_ref is None:
            return new_node
        val_head = key(head_ref.data) if key else head_ref.data
        if (val_head >= val_new and not reverse) or (val_head <= val_new and reverse):
            new_node.next = head_ref
            head_ref.prev = new_node
            return new_node
        current = head_ref
        while current.next is not None:
            val_next = key(current.next.data) if key else current.next.data
            if (val_next < val_new and not reverse) or (val_next > val_new and reverse):
                current = current.next
            else:
                break
        new_node.next = current.next
        if current.next is not None:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current
        return head_ref

    def print_list(self):
        temp = self.head
        res = []
        while temp:
            res.append(str(temp.data))
            temp = temp.next
        print(" <-> ".join(res) if res else "Список пуст")

data = [round(random.uniform(0, 100), 2) for _ in range(8)]
dll = DoublyLinkedList()
for x in data: dll.append(x)
dll.sort()
dll.print_list()
