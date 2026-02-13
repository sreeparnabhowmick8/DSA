class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1={'q','w','e','r','t','y','u','i','o','p'}
        r2={'a','s','d','f','g','h','k','j','l'}
        r3={'z','x','c','v','b','n','m'}
        
        s=[]
        for i in range(len(words)):
            c=words[i].lower()
            s1=s2=s3=0
            for j in range(len(c)):
                if c[j] in r1:
                    s1+=1
                if c[j] in r2:
                    s2+=1
                if c[j] in r3:
                    s3+=1
            if(s1==len(c) or s2==len(c) or s3==len(c)):
                s.append(words[i])
        return s                      
        