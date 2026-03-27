class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        # BRUTE FORCE
        alpha = "abcdefghijklmnopqrstuvwxyz"
        cnt=0
        largest = 1
        for i in range(0,len(s)):
            for j in range(1,len(s)):
                if s[i:j+1] in alpha:
                    cnt=len(s[i:j+1])
                largest =max(largest,cnt)
        return largest

        # OPTIMAL CODE
        alpha="abcdefghijklmnopqrstuvwxyz"
        i=0
        j=1
        res=0
        longest=1
        while(j<len(s)):
            if s[i:j+1] in alpha:
                res=(j-i)+1
                j+=1
                longest=max(longest,res)
            else:
                res=0
                i=j
                j=i+1
        return longest
