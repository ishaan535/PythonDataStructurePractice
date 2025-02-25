from logging import lastResort


class MinHeap:
    def __init__(self, capacity, nums=None):
        self.capacity = capacity
        self.size = 0
        self.arr = []

        if nums:
            self.arr = nums[:]
            self.size = len(nums)

            last_non_leaf_index = int((self.size-2)/2)

            for i in range(last_non_leaf_index, -1, -1):
                self.heapify(i)


    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def heapify(self, index):
        left = 2*index + 1
        right = 2*index + 2
        smallest = index

        if left<self.size and self.arr[left]<self.arr[smallest] :
            smallest = left

        if right<self.size and self.arr[right]<self.arr[smallest]:
            smallest = right

        if smallest != index:
            self.swap(index, smallest)
            self.heapify(smallest)

    def insert_helper(self, index):
        parent = (index-1)//2
        if parent >= 0 and self.arr[parent]>self.arr[index]:
            self.swap(parent, index)
            self.insert_helper(parent)

    def insert(self, data):
        if self.size < self.capacity:
            self.arr.append(data)
            self.size += 1
            self.insert_helper(self.size - 1)

    def extract_min(self):
        if self.size == 0:
            print("Heap is empty.")
            return None
        min_val = self.arr[0]
        self.arr[0] = self.arr[self.size - 1]
        self.size -= 1
        self.arr.pop()
        self.heapify(0)
        return min_val

    def print_heap(self):
        print(" ".join(map(str,self.arr)))

if __name__ == "__main__":
    arr = [5,10,3,20,7,8,30]
    minheap = MinHeap(20, arr)
    minheap.print_heap()
    minheap.insert(23)
    minheap.print_heap()
    print(minheap.extract_min())
    minheap.print_heap()