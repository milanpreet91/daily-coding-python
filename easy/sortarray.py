class Solution:
    def merge(self, first: List[int], second: List[int])->List[int]:
        i = 0
        j = 0
        k = 0
        end1 = len(first)
        end2 = len(second)
        while i < end1 and j < end2:
            if first[i] < second[j]:
                arr[k] = first[i]
                i+=1
            else:
                arr[k] = second[j]
                j+=1
            k += 1
        while i < end1:
            arr[k] = first[i]
        while j < end2:
            arr[k] = second[j]
        return arr

    def sort(self, nums: List[int]): 
        if len(arr) <= 1:
            return

        mid = (start+end)/2
        first = sort(nums[start:mid])
        second = sort(nums, [mid+1:end])
        arr = merge(first, second)
        return arr

    def merge_sort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = sort(num[0:n])
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = merge_sort(nums)
        return nums
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

        ##Merge Sort ## 
        merge_sort(nums)
