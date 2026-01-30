class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return '0'
        if num<0:
            num=num & 0xFFFFFFFF
        res=[]
        hexachars='0123456789abcdef'
        while(num>0):
            res.append(hexachars[num%16])
            num//=16
        return "".join(reversed(res))            
        