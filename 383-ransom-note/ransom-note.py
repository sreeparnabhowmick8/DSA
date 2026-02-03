class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = {}
        maga = {}

        for ch in ransomNote:
            ran[ch] = ran.get(ch, 0) + 1

        for ch in magazine:
            maga[ch] = maga.get(ch, 0) + 1

        for ch in ran:
            if ch not in maga or ran[ch] > maga[ch]:
                return False

        return True
        # ran={}
        # maga={}
        # if(len(ransomNote)==1 and len(magazine)==1):
        #     for i in ransomNote:
        #         if i not in magazine:
        #             return False
        # for i in ransomNote.split():
        #     ran[i]=ran.get(i,0)+1
        # for i in magazine.split():
        #     maga[i]=maga.get(i,0)+1
        # for i in ran.keys():
        #     # if i not in maga:
        #     #     return False
        #     if(ran[i]!=maga[i]):
        #         return False
        # return True  ran = {}
                          
        