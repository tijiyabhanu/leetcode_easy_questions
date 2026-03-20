class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # BRUTE FORCE APPROACH
        k=k%len(arr)
        if k==0:
            return arr
        temp=[]
        for i in range(len(arr)-k,len(arr)):
            temp.append(arr[i])
        
        for i in range(0,len(arr)-k+1):
            temp.append(arr[i]) 
        # print(temp)

        for i in range(0,len(arr)):
            arr[i]=temp[i]
        return arr 
        # OPTIMAL APPROACH 
        k = k%len(arr) 
        
        arr[:]=arr[::-1]
        arr[:]=arr[0:k][::-1]+arr[k:len(arr)][::-1]
        return arr
