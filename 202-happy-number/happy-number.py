class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
        
            seen.add(n)
        
            sum1 = 0
            for digit in str(n):
                sum1 += int(digit) ** 2
        
            n = sum1

        return True           
        