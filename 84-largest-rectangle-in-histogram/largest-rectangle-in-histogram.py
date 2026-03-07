class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rightarr=[]
        stack=[]
        n=len(heights)
        for i in range(n-1,-1,-1):
            while(len(stack)>0 and heights[i]<=heights[stack[-1]]):
                stack.pop()
            if(len(stack)==0):
                rightarr.append(n)
            else:
                rightarr.append(stack[-1])
            stack.append(i)
        rightarr=rightarr[::-1]
        while(len(stack)>0):
            stack.pop()
        leftarr=[]    
        for i in range(n):
            while(len(stack)>0 and heights[i]<=heights[stack[-1]]):
                stack.pop()
            if(len(stack)==0):
                leftarr.append(-1)
            else:
                leftarr.append(stack[-1])
            stack.append(i) 
        ans=0
        for i in range(n):
            width=rightarr[i]-leftarr[i]-1
            currarea=heights[i]*width
            ans=max(ans,currarea)
        return ans          

        