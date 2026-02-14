class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        s.split()
        i=0
        while(i<len(s)):
            if(s[i]=='('or s[i]=='{'or s[i]=='['):
                stack.append(s[i])
            else:
                if(len(stack)==0):
                    return False    
                if((s[i]==')'and stack[-1]=='(') or (s[i]=='}'and stack[-1]=='{') or (s[i]==']'and stack[-1]=='[')):
                    stack.pop()
                else:
                    return False    
            i+=1
        if(len(stack)==0):
            return True
        else:
            return False            
        
            

        