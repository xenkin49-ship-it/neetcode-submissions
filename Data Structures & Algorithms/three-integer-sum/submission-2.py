class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sorted_arr=sorted(nums)
        for i in range(len(sorted_arr)):
            if i>0 and sorted_arr[i]==sorted_arr[i-1]:
                continue
            target=-sorted_arr[i]
            j,k=i+1,len(sorted_arr)-1
            while j<k:
                if sorted_arr[j]+sorted_arr[k]==target:
                    res.append([sorted_arr[i], sorted_arr[j],sorted_arr[k]])
                    j+=1
                    k-=1
                    while j<k and sorted_arr[j]==sorted_arr[j-1]:
                        j+=1
                    while k>j and sorted_arr[k]==sorted_arr[k+1]:
                        k-=1
                elif sorted_arr[j]+sorted_arr[k]>target:
                    k-=1
                else:
                    j+=1
        return res