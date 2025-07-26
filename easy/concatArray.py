def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        add = 0
        for i in range(2):
            for j in range(n):
                ans.append(nums[j])
        return ans