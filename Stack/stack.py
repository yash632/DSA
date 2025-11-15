class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def display(self):
        print(self.data)









# ------------------------
# FULL STACK TESTING
# ------------------------

s = Stack()
print("\n--- Test 1: Push ---")
s.push(10)
s.push(20)
s.push(30)
s.display()                # [10, 20, 30]
print("Size:", s.size())   # 3
print("Empty:", s.is_empty())  # False
print("Peek:", s.peek())   # 30

print("\n--- Test 2: Pop ---")
print("Pop:", s.pop())     # 30
s.display()                # [10, 20]
print("Peek:", s.peek())   # 20
print("Size:", s.size())   # 2

print("\n--- Test 3: Push + Pop mix ---")
s.push(40)                 # [10,20,40]
s.push(50)                 # [10,20,40,50]
s.display()
print("Pop:", s.pop())     # 50
s.display()                # [10,20,40]
print("Peek:", s.peek())   # 40

print("\n--- Test 4: Pop until empty ---")
s.pop()   # 40
s.pop()   # 20
s.pop()   # 10
s.display()                # []
print("Empty:", s.is_empty())   # True
print("Peek:", s.peek())        # None
print("Pop empty:", s.pop())    # None

print("\n--- Test 5: Push after empty ---")
s.push(999)
s.display()                # [999]
print("Peek:", s.peek())   # 999
print("Size:", s.size())   # 1

print("\n--- Test 6: More operations ---")
s.push(111)
s.push(222)
s.pop()     # 222
s.push(333)
s.display()  # [999,111,333]
print("Peek:", s.peek())   # 333
print("Size:", s.size())   # 3
