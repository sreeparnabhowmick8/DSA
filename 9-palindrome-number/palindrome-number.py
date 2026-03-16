class Solution:
    def isPalindrome(self, x: int) -> bool:
        v=x
        rev=0
        while(x>0):
            rev=rev*10+(x%10)
            x=x//10
        if(v==rev):
            return True
        else:
            return False    
        