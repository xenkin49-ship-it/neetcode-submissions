class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache={}
        def dfs(rem):
            if rem==0:
                return 0
            if rem<0:
                return float("inf")
            if rem in cache:
                return cache[rem]
            cache[rem]=1+min(dfs(rem - c) for c in coins)
            return cache[rem]
        res=dfs(amount)
        return res if res!=float("inf") else -1