class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res,quad=[],[]
        def kSum(k,start,target):
            if k==2:
                i,j=start,len(nums)-1
                while i<j:
                    if nums[i]+nums[j]==target:
                        res.append(quad+[nums[i],nums[j]])
                        i+=1
                        j-=1
                        while i<j and nums[i]==nums[i-1]:
                            i+=1
                        while i<j and nums[j]==nums[j+1]:
                            j-=1
                    elif nums[i]+nums[j]<target:
                        i+=1
                    else:
                        j-=1
                return

            for i in range(start,len(nums)-k+1):
                if i>start and nums[i]==nums[i-1]:
                    continue
                quad.append(nums[i])
                kSum(k-1,i+1,target-nums[i])
                quad.pop()
        kSum(4,0,target)
        return res