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

    def sort(self):
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
            sorted_list = self._sorted_insert(sorted_list, current)
            current = next_node
        
        self.head = sorted_list
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = self.head

    def _sorted_insert(self, head_ref, new_node):
        if head_ref is None or head_ref.data >= new_node.data:
            new_node.next = head_ref
            return new_node
        current = head_ref
        while current.next is not None and current.next.data < new_node.data:
            current = current.next
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


print("\n--- Лаба 17: Циклический список ---")
data = [round(random.uniform(0, 100), 2) for _ in range(10)]
print("Исходный массив:", data)

cll = CircularLinkedList()
for x in data:
    cll.append(x)

print("Список до сортировки:")
cll.print_list()

cll.sort()
print("Список после сортировки:")
cll.print_list()

cll.remove(data[0])
print(f"Список после удаления элемента {data[0]}:")
cll.print_list()
