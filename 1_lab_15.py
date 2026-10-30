import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next

    def sort(self, key=None, reverse=False):
        sorted_list = None
        current = self.head
        while current is not None:
            next_node = current.next
            sorted_list = self._sorted_insert(sorted_list, current, key, reverse)
            current = next_node
        self.head = sorted_list

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
        temp = self.head
        res = []
        while temp:
            res.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(res) if res else "Список пуст")

data = [round(random.uniform(0, 100), 2) for _ in range(8)]
sll = SinglyLinkedList()
for x in data: sll.append(x)
sll.sort()
sll.print_list()
