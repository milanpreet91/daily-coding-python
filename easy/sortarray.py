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

    def sort(self, arr: List[int]) -> List[int]: 
        if len(arr) <= 1:
            return arr

        mid = (len(arr))//2
        print(f"mid : {mid}")
        first = self.sort(arr[:mid])
        print(f"first half is: {first}")
        second = self.sort(arr[mid:])
        print(f"second half is: {second}")
        arr = self.merge(first, second)
        print(f"merge gives: {arr}")
        return arr

    def merge_sort(self, nums: List[int]):
        n = len(nums)
        return self.sort(nums[0:n])

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ##Merge Sort ## 
        return self.merge_sort(nums)
        ############
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

        
