class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        seen=set()
        j=0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[j])
                j+=1
            seen.add(s[i])
            res=max(res,i+1-j)
        return res