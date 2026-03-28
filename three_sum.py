class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # BRUTE IS USING 3 FOR LOOPS
        # BETTER SOLUTION USING HASHING
        res=set()
        for i in range(0,len(nums)):
            seen=set()
            for j in range(i+1,len(nums)):
                k=-(nums[i]+nums[j])
                if k in seen:
                    temp = tuple(sorted([nums[i],nums[j],k]))
                    res.add(temp)
                else:
                    seen.add(nums[j])
        return list(res)
        # OPTIMAL ONE
        res=[]
        nums.sort()
        for i in range(0,len(nums)):
            j=i+1
            k=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum==0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while (j<k) and nums[j]==nums[j-1]:
                            j+=1
                    while (j<k) and nums[k]==nums[k+1]:
                            k-=1
                elif sum<0:
                    j+=1
                    while (j<k) and nums[j]==nums[j-1]:
                            j+=1
                else:
                    k-=1
                    while (j<k) and nums[k]==nums[k+1]:
                            k-=1
        return res
