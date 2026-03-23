class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic={}
        l,r,maxlen=0,0,0
        n=len(fruits)
        while(r<n):
            dic[fruits[r]]=dic.get(fruits[r],0)+1
            while len(dic) > 2:
                dic[fruits[l]] -= 1
                if dic[fruits[l]] == 0:
                    dic.pop(fruits[l])
                l += 1   # ✅ moved inside

            maxlen = max(maxlen, r - l + 1)
            r += 1

        return maxlen                             

        