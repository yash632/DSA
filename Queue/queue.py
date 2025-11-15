class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.is_empty():
            return None    
        return self.data.pop(0)

    def peek(self):
        return self.data[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)
    
    def display(self):
        print(self.data)









# ------------------------
# FULL QUEUE TESTING
# ------------------------

q = Queue()
print("\n--- Test 1: Enqueue ---")
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()               # [10, 20, 30]
print("Size:", q.size())  # 3
print("Empty:", q.is_empty())  # False
print("Peek:", q.peek())  # 10

print("\n--- Test 2: Dequeue ---")
print("Dequeue:", q.dequeue())   # 10
q.display()                      # [20, 30]
print("Peek:", q.peek())         # 20
print("Size:", q.size())         # 2

print("\n--- Test 3: More enqueue + dequeue ---")
q.enqueue(40)                    # [20, 30, 40]
q.enqueue(50)                    # [20, 30, 40, 50]
q.display()
print("Dequeue:", q.dequeue())   # 20
q.display()                      # [30, 40, 50]

print("\n--- Test 4: Dequeue until empty ---")
q.dequeue()   # 30
q.dequeue()   # 40
q.dequeue()   # 50
q.display()   # []
print("Empty:", q.is_empty())    # True
print("Peek:", q.peek())         # None
print("Dequeue empty:", q.dequeue())  # None

print("\n--- Test 5: Enqueue after empty ---")
q.enqueue(999)
q.display()                      # [999]
print("Peek:", q.peek())         # 999
print("Size:", q.size())         # 1

print("\n--- Test 6: Mixed operations ---")
q.enqueue(111)
q.enqueue(222)
q.dequeue()   # 999
q.enqueue(333)
q.display()   # [111, 222, 333]
print("Peek:", q.peek())         # 111
print("Size:", q.size())         # 3
