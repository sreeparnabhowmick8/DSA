class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # ans=""
        # list=['1','2','3','4','5','6','7','8','9']
        # for i in s:
        #     if i in list:
        #         ans+=ans
        #         if(len(ans)==k):
        #             break
        #     else:
        #         ans+=i
        # for i in range(len(ans)):
        #     if(i==(k-1)%len(ans)):
        #         return ans[i]
        lengths = [0]
    
    # 1. Build the stack of lengths
        for char in s:
            if char.isdigit():
            # Multiply the last known length
                lengths.append(lengths[-1] * int(char))
            else:
            # Add 1 to the last known length
                lengths.append(lengths[-1] + 1)

    # 2. Walk backwards through the string and the stack
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
        
        # Adjust k to fit within the current total length
            k %= lengths[i + 1]
        
        # If k is 0 and we are at a letter, that's our target!
            if k == 0 and char.isalpha():
                return char

        