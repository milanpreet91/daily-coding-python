class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        min_s = strs[0]
        if len(strs) == 1:
            return strs[0]
            
        for s in strs:
            if len(s) < len(min_s):
                min_s = s
                if len(min_s) == 0:
                    return min_s

        min_len = len(min_s)
        for i in range(min_len):
            ch = min_s[i]
            for s in strs:
                if(s[i]) != ch:
                    return res
            res = res+ch
        return res