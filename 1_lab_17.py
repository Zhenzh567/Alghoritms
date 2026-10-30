import random

class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = CNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def remove(self, key):
        if self.head is None:
            return
        if self.head.data == key:
            if self.head.next == self.head:
                self.head = None
                return
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return
        prev = self.head
        current = self.head.next
        while current != self.head:
            if current.data == key:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def sort(self, key=None, reverse=False):
        if not self.head or self.head.next == self.head:
            return
        last = self.head
        while last.next != self.head:
            last = last.next
        last.next = None
        sorted_list = None
        current = self.head
        while current is not None:
            next_node = current.next
            sorted_list = self._sorted_insert(sorted_list, current, key, reverse)
            current = next_node
        self.head = sorted_list
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = self.head

    def _sorted_insert(self, head_ref, new_node, key, reverse):
        val_new = key(new_node.data) if key else new_node.data
        if head_ref is None:
            new_node.next = None
            return new_node
        val_head = key(head_ref.data) if key else head_ref.data
        if (val_head >= val_new and not reverse) or (val_head <= val_new and reverse):
            new_node.next = head_ref
            return new_node
        current = head_ref
        while current.next is not None:
            val_next = key(current.next.data) if key else current.next.data
            if (val_next < val_new and not reverse) or (val_next > val_new and reverse):
                current = current.next
            else:
                break
        new_node.next = current.next
        current.next = new_node
        return head_ref

    def print_list(self):
        if not self.head:
            print("Список пуст")
            return
        temp = self.head
        res = []
        while True:
            res.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(res) + " -> (цикл)")

data = [round(random.uniform(0, 100), 2) for _ in range(8)]
cll = CircularLinkedList()
for x in data: cll.append(x)
cll.sort()
cll.print_list()
