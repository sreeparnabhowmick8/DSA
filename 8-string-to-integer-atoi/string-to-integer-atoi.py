class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        i = 0
        sign = 1
        ans = 0

        INT_MAX = 2147483647
        INT_MIN = -2147483648

        # sign handling
        if s[i] == '-':
            sign = -1
            i += 1

        elif s[i] == '+':
            i += 1

        # digit conversion
        while i < len(s) and s[i].isdigit():

            digit = int(s[i])

            # overflow check
            if ans > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            ans = ans * 10 + digit
            i += 1

        return sign * ans

                          

               

                    
        
        