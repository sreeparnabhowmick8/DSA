from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # s.split()
        # freq=Counter(s)
        # s1=min(freq)
        # str1=""
        # for i in freq.values():
        #     if i==s1:
        #         str1+=i
        #         break
        # for i in s:
        #     if i not in str1:
        #         str1+=i
        # return str1 
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        stack = []
        seen = set()
        for ch in s:
            freq[ch] -= 1
            if ch in seen:
                continue
            while stack and ch < stack[-1] and freq[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(ch)
            seen.add(ch)
        return "".join(stack)               



        