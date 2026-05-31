class Solution:
    def asteroidsDestroyed(self, mass: int, aster: List[int]) -> bool:
        sum1=mass
        aster.sort()
        for i in aster:
            if(sum1<i):
                return False
            else:
                sum1+=i
        return True            
        