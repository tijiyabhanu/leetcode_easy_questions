class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        
        def backtrack(sub,used):
            if len(sub)==len(nums):
                result.append(sub[:])
                return
            for i in range(len(nums)):
                if used[i]==1:
                    continue
                sub.append(nums[i])
                used[i]=1
                backtrack(sub,used)
                sub.pop()
                used[i]=0
        backtrack([],[0]*len(nums))
        return result
        
