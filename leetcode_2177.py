class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # BRUTE FORCE
        j=2
        sum=(j-1)+j+(j+1)
        res=[]
        while sum<=num:
            if sum==num:
                res.append(i)
                res.append(j)
                res.append(k)
                break
            elif sum<num:
                i=j-1
                j+=1
                k=j+1
                sum=i+j+k    
        return res
        # ANOTHER BRUTE FORCE
        res=[]
        for i in range(2,num):
            if (3*i)==num:
                res.extend([i-1,i,i+1])
                break
            elif (3*i)>num:
                break
        return res
        # OPTIMAL CODE
        rem = num%3
        quo = num//3
        if rem==0:
            return [quo-1,quo,quo+1]
        else:
            return []
