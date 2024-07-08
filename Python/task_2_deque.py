from collections import deque


class CircularBufferDeque:
    def __init__(self, size):
        self.buffer = deque(maxlen=size)

    def is_full(self):
        return len(self.buffer) == self.buffer.maxlen

    def is_empty(self):
        return len(self.buffer) == 0

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Buffer is full")
        self.buffer.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty")
        return self.buffer.popleft()


buffer = CircularBufferDeque(5)
buffer.enqueue(1)
buffer.enqueue(2)
print(buffer.dequeue())  # 1
print(buffer.dequeue())  # 2
