from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
    
    # sort characters by decreasing frequency
        chars = sorted(freq.keys(), key=lambda c: -freq[c])
    
    # build result
        return "".join(c * freq[c] for c in chars)        
        