class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # BRUTE IS USING ANY SORTING ALGORITHM
        # BETTER SOLUTION
        zero=0
        ones=0
        twos=0
        for i in nums:
            if i==0:
                zero+=1
            elif i==1:
                ones+=1
            else:
                twos+=1
        for i in range(0,zero):
            nums[i]=0
        for i in range(zero,ones+zero):
            nums[i]=1
        for i in range(zero+ones,twos+ones+zero):
            nums[i]=2

        # OPTIMAL ONE (NATIONAL DUTCH FLAG ALGORITHM)
        low=0
        mid=0
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1
