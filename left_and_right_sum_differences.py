class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum=[0]*len(nums)
        rightsum=[0]*len(nums)
        res=[0]*len(nums)
        total = sum(nums)
        for i in range(1,len(nums)):
            leftsum[i]=leftsum[i-1]+nums[i-1]
        for i in range(0,len(nums)-1):
            rightsum[i]=total-(nums[i]+leftsum[i])
        for i in range(0,len(nums)):
            res[i]=abs(leftsum[i]-rightsum[i])
        return res
