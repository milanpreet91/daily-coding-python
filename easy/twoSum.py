def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        #### “I started with a sorted two-pointer version because it's clean and intuitive. But since we need original indices, I stored (index, value) pairs before sorting. 
        For optimal performance, I’d also consider a hash map approach to achieve O(n).”####
        
        #TC: O(nlogn) + O(n)
        #SC: O(n)
        sort_nums = sorted(nums)
        i = 0
        j = len(nums)-1
        while i<j:
            sum_val = sort_nums[i] + sort_nums[j]
            if  sum_val > target:
                j = j-1
            elif sum_val == target:
                res = {sort_nums[i],sort_nums[j]}
                break
            else:
                i = i+1
        final_res = []
        for i in range(len(nums)):
            if nums[i] in res:
                final_res.append(i)
        return final_res       
        '''
        #HashMap version using dictionary
        #TC: O(n)
        #SC: O(n)
        a_dict = {}
        for i, num in enumerate(nums):
            complement = target-num
            if complement in a_dict:
                return [a_dict[complement], i]
            a_dict[num] = i 