class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        for i in s:
            if i=='#'and len(stack1)!=0:
                stack1.pop()
            if(i!='#'):
                stack1.append(i)
        for i in t:
            if i=='#'and len(stack2)!=0:
                stack2.pop()
            if(i!='#'):    
                stack2.append(i)
        if(len(stack1)==0 and len(stack2)==0):
            return True
        elif(len(stack1)!=len(stack2)):
            return False
        else:
            for i in range(len(stack1)):
                if(stack1[i]!=stack2[i]):
                    return False
            return True            



        