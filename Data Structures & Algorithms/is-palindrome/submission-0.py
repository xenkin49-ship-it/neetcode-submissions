class Solution:
    def isPalindrome(self, s: str) -> bool:
        joined = [c.lower() for c in s if c.isalnum()]
        n=len(joined)
        for i in range(n//2):
            if joined[i]!=joined[n-1-i]:
                return False
        return True