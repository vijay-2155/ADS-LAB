# Manual implementation of Min and Max Heap using arrays

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def delete(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        n = len(self.heap)

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def delete(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        n = len(self.heap)

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)


# -------- Main Program --------
print("Min Heap Operations:")
min_heap = MinHeap()
for val in [30, 20, 40, 10, 25, 50]:
    min_heap.insert(val)
print("Min Heap:", min_heap.heap)
deleted = min_heap.delete()
print("Deleted element:", deleted)
print("Heap after deletion:", min_heap.heap)

print("\nMax Heap Operations:")
max_heap = MaxHeap()
for val in [30, 20, 40, 10, 25, 50]:
    max_heap.insert(val)
print("Max Heap:", max_heap.heap)
deleted = max_heap.delete()
print("Deleted element:", deleted)
print("Heap after deletion:", max_heap.heap)
