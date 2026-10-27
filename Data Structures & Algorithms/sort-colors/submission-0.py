class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0]*3
        for num in nums:
            if num == 0:
                count[0] +=1
            elif num == 1:
                count[1] +=1
            else:
                count[2]+=1
        index = 0
        for i in range(3):
            while count[i]:
                nums[index] = i
                count[i] -= 1
                index +=1