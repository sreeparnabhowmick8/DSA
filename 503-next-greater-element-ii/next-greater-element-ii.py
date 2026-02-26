class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        stack=[]
        ans=[0]*n
        for i in range(2*n-1,-1,-1):
            while(len(stack)>0 and nums[stack[-1]]<=nums[i%n]):
                stack.pop()
            if(len(stack)==0):
                stack.append(i%n)
                ans[i%n]=-1
            else:
                ans[i%n]=nums[stack[-1]]
                stack.append(i%n)
        return ans                
                        
        