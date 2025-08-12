##Time complexity ##
# array can be divided by 2^x i.e. n / (2^x) to become 1
# To get x, we log both sides. So if x = logn, means height of tree is logn. 
# We need to merge n elements at each level, 
# so total work is (num of actions at each level)*(num of levels)
# TC: nlogn
'''
bubble sort: O(n^2)
merge sort: O(nlogn)
quick sort: O(nlogn)
heap sort: O(nlogn)
'''
import sys
class Solution:
    def merge(self, first: List[int], second: List[int])->List[int]:
        i = 0
        j = 0
        k = 0
        end1 = len(first)
        end2 = len(second)
        arr = []
        while i < end1 and j < end2:
            if first[i] < second[j]:
                arr.append(first[i])
                i+=1
            else:
                arr.append(second[j])
                j+=1
            k += 1

        while i < end1:
            arr.append(first[i])
            i += 1
            k += 1
        while j < end2:
            arr.append(second[j])
            j += 1
            k += 1
        return arr

    def merge_sort(self, arr: List[int]) -> List[int]: 
        if len(arr) <= 1:
            return arr

        mid = (len(arr))//2
        first = self.merge_sort(arr[:mid])
        second = self.merge_sort(arr[mid:])
        arr = self.merge(first, second)
        return arr

    ## Quick Sort ##
    def quicksort(self, arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[-1]
        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]
        return self.quicksort(left) + [pivot] + self.quicksort(right)
    #########################

    ### Heap Sort ###
    def swapmax(self, arr, p, l, r, n):
        largest = p
        if r < n and arr[r] > arr[largest]:
            largest = r
        if l < n and arr[l] > arr[largest]:
            largest = l
        if largest != p: 
            arr[largest], arr[p] = arr[p], arr[largest]
            self.heapify(arr, largest, n)

    def swap(self, arr, a, b):
        return (arr[b], arr[a])

    def heapify(self, arr, i, end):
        if i >= end:
            return
        left = 2*i + 1
        right = 2*i + 2
        self.swapmax(arr, i, left, right, end)
        #if swapped:
            #print(f"new arr: {arr}")
            #self.heapify(arr, ind)

    def buildmaxheap(self, arr: List[int])->List[int]:
        n = len(arr)
        start = n//2 - 1
        stop = -1
        step = -1
        for i in range(start, stop, step):
            #print(f"i: {i}")
            self.heapify(arr, i, n)
        return arr

    def heapsort(self, arr):
        arr = self.buildmaxheap(arr)
        #print(f"arr post max heap built: {arr}")
        last = len(arr) - 1
        while last > 0:
            arr[last], arr[0] = self.swap(arr, last, 0)
            #print(f"arr post swap: {arr}")
            self.heapify(arr, 0, last)
            #print(f"arr post heapify: {arr}")
            last -= 1
        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        sys.setrecursionlimit(20000) 
        n = len(nums)
        ##Merge Sort ## 
        #return self.merge_sort(nums[0:n])
        ############
        #return self.quicksort(nums[0:n])
        return self.heapsort(nums)
        '''
        ##BubbleSort## O(n^2)
        
        for i in range(n-1):
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    temp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = temp
        return nums
        
        ##InsertionSort## O(n^2)
        for i in range(1,n):
            for j in range(i-1, -1, -1):
                if nums[j+1] < nums[j]:
                    temp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = temp
        return nums
        '''

        
