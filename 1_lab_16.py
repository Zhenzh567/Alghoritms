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

    def sort(self):
        if not self.head or not self.head.next:
            return
        sorted_list = None
        current = self.head
        while current is not None:
            next_node = current.next
            sorted_list = self._sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def _sorted_insert(self, head_ref, new_node):
        new_node.prev = None
        new_node.next = None
        
        if head_ref is None or head_ref.data >= new_node.data:
            new_node.next = head_ref
            if head_ref is not None:
                head_ref.prev = new_node
            return new_node
        
        current = head_ref
        while current.next is not None and current.next.data < new_node.data:
            current = current.next
        
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


print("\n--- Лаба 16: Двусвязный список ---")
data = [round(random.uniform(0, 100), 2) for _ in range(10)]
print("Исходный массив:", data)

dll = DoublyLinkedList()
for x in data:
    dll.append(x)

print("Список до сортировки:")
dll.print_list()

dll.sort()
print("Список после сортировки:")
dll.print_list()

dll.remove(data[0])
print(f"Список после удаления элемента {data[0]}:")
dll.print_list()
