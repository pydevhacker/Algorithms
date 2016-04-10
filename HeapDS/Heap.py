class MinHeap:

    INFMIN = -999999

    def __init__(self, capacity=0):
        self.capacity = capacity
        self.heapSize = 0
        self.arr = [0]*capacity

    def parent(self, i):
        return (i-1)//2

    def left(self, i):
        return 2*i+1

    def right(self, i):
        return 2*i+2

    def insert(self, key):
        if self.heapSize == self.capacity:
            print("Capacity is full")
            return

        self.heapSize += 1
        i = self.heapSize - 1
        self.arr[i] = key

        while i >= 0 and self.arr[self.parent(i)] > self.arr[i]:
            self.arr[i], self.arr[self.parent(i)] = self.arr[self.parent(i)], self.arr[i]
            i = self.parent(i)

    def decreaseKey(self, i, newValue):
        a = self.arr
        a[i] = newValue
        while i != 0 and a[self.parent(i)] > a[i]:
            a[i], a[self.parent(i)] = a[self.parent(i)], a[i]
            i = self.parent(i)

    def deleteKey(self, i):
        self.decreaseKey(i, -9999999)
        self.extractMin()

    def extractMin(self):
        if self.heapSize <= 0:
            return
        if self.heapSize == 1:
            self.heapSize -= 1
            return self.arr[0]

        root = self.arr[0]
        self.arr[0] = self.arr[self.heapSize-1]
        self.heapSize -= 1
        self.minHeapify(0)
        return root

    def minHeapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l<self.heapSize and self.arr[l] < self.arr[smallest]:
            smallest = l
        if r<self.heapSize and self.arr[r] < self.arr[smallest]:
            smallest = r

        if smallest != i:
            self.arr[smallest], self.arr[i] = self.arr[i], self.arr[smallest]
            self.minHeapify(smallest)

    def getMin(self):
        return self.arr[0]

heap = MinHeap(11)
heap.insert(3)
heap.insert(2)
heap.insert(15)
heap.insert(5)
heap.insert(4)
heap.insert(45)

print(heap.extractMin())
print(heap.getMin())
heap.decreaseKey(3, 1)
print(heap.getMin())
