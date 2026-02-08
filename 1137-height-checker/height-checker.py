class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp=sorted(heights)
        n,c=len(heights),0
        for i in range(n):
            if (exp[i]!=heights[i]):
                c+=1
        return c        
        