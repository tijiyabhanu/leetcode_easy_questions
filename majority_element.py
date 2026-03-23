class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # BETTER SOLUTION USING HASHING
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]>(len(nums)//2):
                return i

        # OPTIMAL USING MOORE'S VOTING ALGORITHM
        ele=0
        count=0
        for i in nums:
            if count==0:
                ele=i
                count+=1
            else:
                if ele==i:
                    count+=1
                else:
                    count-=1
        count1=0
        for i in nums:
            if i==ele:
                count1+=1
        if count1 > (len(nums)//2):
            return ele
        return -1
