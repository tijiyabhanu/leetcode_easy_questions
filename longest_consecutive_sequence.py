class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # BRUTE FORCE APPROACH

        longest = 1
        if len(nums)==0:
            return 0
        for i in range(0,len(nums)):
            x = nums[i]
            cnt=1
            while True:
                flag = False
                for j in range(0,len(nums)):
                    if nums[j]==(x+1):
                        cnt+=1
                        x+=1
                        flag = True
                if flag==True:
                    continue
                else:
                    break
            longest = max(longest,cnt)
        return longest

        # BETTER SOLUTION
        nums.sort()
        if len(nums)==0:
            return 0
        cnt=0
        longest = 1
        lastele=float('-inf')
        for i in range(0,len(nums)):
            if nums[i]==lastele:
                continue
            if (nums[i]-1)==lastele:
                cnt+=1
                lastele=nums[i]
            
            elif (nums[i]-1)!=lastele:
                cnt=1
                lastele=nums[i]

            longest=max(longest,cnt)
        return longest

        # OPTIMAL CODE
        longest=1
        if len(nums)==0:
            return 0
        nums = set(nums)
        for i in nums:
            if i-1 in nums:
                continue
            else:
                cnt=1
                while(True):
                    if i+1 in nums:
                        cnt+=1
                        i=i+1
                    else:
                        break
                longest = max(longest,cnt)
        return longest
