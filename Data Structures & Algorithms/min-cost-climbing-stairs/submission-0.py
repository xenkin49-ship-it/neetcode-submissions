class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        cache={}
        def helper(i):
            if i>=n:
                return 0
            if i in cache.keys():
                return cache[i]
            cache[i]=cost[i]+min(helper(i+1),helper(i+2))
            return cache[i]
        return min(helper(0),helper(1))