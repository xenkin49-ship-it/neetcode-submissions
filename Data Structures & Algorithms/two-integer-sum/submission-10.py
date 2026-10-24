class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            indices = {}
            for i, num in enumerate(nums):
                indices[num] = i
            for i, num in enumerate(nums):
                complement = target-num
                if complement in indices and indices[complement]!=i:
                    return [i, indices[complement]]
            return None