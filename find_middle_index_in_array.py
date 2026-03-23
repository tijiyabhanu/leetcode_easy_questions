class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # space optimized code
        ftemp=0
        ltemp=0
        total = sum(nums)
        temp=0
        for i in range(0,len(nums)):
            ftemp+=nums[i]
            ltemp=total-temp
            temp=ftemp
            if abs(ftemp-ltemp)==0:
                return i
        return -1
