class Node:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.s = 0
    
    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.s += 1

    def delete(self, node = 0):
        if self.head and node == 0:
            self.head = self.head.next
            self.s -= 1
            return self.s, self.head
        else:
            current = self.head
            i = 0
            while current and current.next:
                if i == node - 1:
                    current.next = current.next.next
                    self.s -= 1
                    return self.s, self.head
                current = current.next
                i += 1

    def search(self, value):
        current  = self.head
        i = 0
        while current:
            if current.val == value:
                return current.val, i
            current = current.next
            i += 1
        return None

    def display(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    def size(self):
        return self.s


    def is_empty(self):
        return self.s == 0
    



# ------------------------
# FULL LINKED LIST TESTING
# ------------------------

LL = LinkedList()
print("\n--- Test 1: Insert ---")
LL.insert(10)
LL.insert(20)
LL.insert(30)
LL.display()        # 30 -> 20 -> 10
print("Size:", LL.size())
print("Empty:", LL.is_empty())

print("\n--- Test 2: Delete head ---")
LL.delete(0)
LL.display()        # 20 -> 10
print("Size:", LL.size())

print("\n--- Test 3: Insert again + delete middle ---")
LL.insert(40)       # 40 -> 20 -> 10
LL.insert(50)       # 50 -> 40 -> 20 -> 10
LL.delete(2)        # delete '20'
LL.display()        # 50 -> 40 -> 10
print("Size:", LL.size())

print("\n--- Test 4: Delete last node ---")
LL.delete(2)        # delete '10'
LL.display()        # 50 -> 40

print("\n--- Test 5: Search existing element ---")
print(LL.search(40))  # (40, 1)

print("\n--- Test 6: Search non-existing element ---")
print(LL.search(999))  # None

print("\n--- Test 7: Delete out-of-range index ---")
LL.delete(10)       # no crash
LL.display()        # 50 -> 40

print("\n--- Test 8: Delete on empty list ---")
A = LinkedList()
A.delete(0)         # no crash
A.display()         # None

print("\n--- Test 9: Insert after clearing ---")
B = LinkedList()
B.insert(5)
B.delete(0)
B.insert(100)
B.display()         # 100 -> None

print("\n--- Test 10: is_empty check ---")
C = LinkedList()
print(C.is_empty())  # True
C.insert(1)
print(C.is_empty())  # False
