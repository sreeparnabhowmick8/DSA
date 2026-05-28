class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        s=int(dividend/divisor)
        if(s>=2147483648):
            return 2147483647
        else:
            return int(dividend/divisor)
        