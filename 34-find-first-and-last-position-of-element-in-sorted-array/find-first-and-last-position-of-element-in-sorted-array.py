class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r=-1,-1
        counter=0
        n=len(nums)
        if(n==0 or nums[n-1]<target):
            return [l,r]
        for i in range(len(nums)):
            if(nums[i]==target):
                if(counter!=0):
                    r=i
                else:    
                    l=i
                    r=l
                counter+=1
        return [l,r]        
                      
              

            
               
   
   
        