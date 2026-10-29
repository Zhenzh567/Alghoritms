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

    def sort(self):
        sorted_list = None
        current = self.head
        while current is not None:
            next_node = current.next
            sorted_list = self._sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

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
        temp = self.head
        res = []
        while temp:
            res.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(res) if res else "Список пуст")

print("--- Лаба 15: Односвязный список ---")
data = [round(random.uniform(0, 100), 2) for _ in range(10)]
print("Исходный массив:", data)

sll = SinglyLinkedList()
for x in data:
    sll.append(x)

print("Список до сортировки:")
sll.print_list()

sll.sort()
print("Список после сортировки:")
sll.print_list()

sll.remove(data[0])
print(f"Список после удаления элемента {data[0]}:")
sll.print_list()
