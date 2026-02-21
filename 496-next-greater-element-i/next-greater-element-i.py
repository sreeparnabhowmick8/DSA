class Solution:
    def nextGreaterElement(self, num1: List[int], num2: List[int]) -> List[int]:
        stack=[]
        ans=[]
        res=[]
        for i in range(len(num2)-1,-1,-1):
            while(len(stack)>0 and num2[i]>stack[-1]):
                stack.pop()
            if(len(stack)==0):
                ans.append(-1) 
                stack.append(num2[i])
            else:
                ans.append(stack[-1])
                stack.append(num2[i]) 
        ans1=ans[::-1] 
        dic={}
        for i in range(len(num2)):
            dic[num2[i]]=ans1[i]
        for i in num1:
            res.append(dic[i])
        return res
        