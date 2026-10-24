class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setara = set(nums)
        return True if len(setara) != len(nums) else False