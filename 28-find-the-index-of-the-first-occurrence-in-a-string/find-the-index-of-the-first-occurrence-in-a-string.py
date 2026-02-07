class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(len(haystack)==len(needle)):
            if(haystack==needle):
                return 0 
        for i in range(len(haystack)):
            if(needle[0]==haystack[i]):
                if(haystack[i:len(needle)+i]==needle[:len(needle)]):
                    return i
        return -1                  
        