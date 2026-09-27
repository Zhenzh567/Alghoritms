import os


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def remove(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next
        return False

    def sort(self, reverse=False):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        values.sort(reverse=reverse)
        self.head = None
        self.tail = None
        for v in values:
            self.append(v)

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


if not os.path.exists("input.txt"):
    with open("input.txt", "w", encoding="utf-8") as f:
        f.write("5.2 2.1 4.8 1.3 3.7")

with open("input.txt", "r", encoding="utf-8") as f:
    nums = [float(x) for x in f.read().split()]

lst = DoublyLinkedList()
for n in nums:
    lst.append(n)

print("Исходный:")
lst.display()

lst.sort(reverse=False)

print("Отсортированный:")
lst.display()

lst.remove(2.1)
print("После удаления 2.1:")
lst.display()
