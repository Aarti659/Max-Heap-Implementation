import sys

class max_heap:
    def __init__(self, size_limit):
        self.size_limit = size_limit
        self.cur_size = 0
        self.Heap = [0] * (self.size_limit + 1)
        self.Heap[0] = sys.maxsize
        self.root = 1


    def swapnodes(self, node1, node2):
        self.Heap[node1], self.Heap[node2] = self.Heap[node2], self.Heap[node1]


    def max_heapify(self, j):


        if not (j >= (self.cur_size // 2) and j <= self.cur_size):
            if (self.Heap[j] < self.Heap[2 * j] or self.Heap[j] < self.Heap[(2 * j) + 1]):
                if self.Heap[2 * j] > self.Heap[(2 * j) + 1]:

                    self.swapnodes(j, 2 * j)
                    self.max_heapify(2 * j)

                else:

                    self.swapnodes(j, (2 * j) + 1)
                    self.max_heapify((2 * j) + 1)


    def heappush(self, element):
        if self.cur_size >= self.size_limit:
            return
        self.cur_size += 1
        self.Heap[self.cur_size] = element
        current = self.cur_size
        while self.Heap[current] > self.Heap[current // 2]:
            self.swapnodes(current, current // 2)
            current = current // 2


    def heappop(self):
        last = self.Heap[self.root]
        self.Heap[self.root] = self.Heap[self.cur_size]
        self.cur_size -= 1
        self.max_heapify(self.root)
        return last


    def build_heap(self):
        for j in range(self.cur_size // 2, 0, -1):
            self.max_heapify(j)


    def print_heap(self):
        for j in range(1, (self.cur_size // 2) + 1):
            print("Parent Node is " + str(self.Heap[j]) + " Left Child is " + str(
                self.Heap[2 * j]) + " Right Child is " + str(self.Heap[2 * j + 1]))


maxHeap = max_heap(10)
maxHeap.heappush(29)
maxHeap.heappush(8)
maxHeap.heappush(9)
maxHeap.heappush(5)
maxHeap.heappush(13)
maxHeap.print_heap()



