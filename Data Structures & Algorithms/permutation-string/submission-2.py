class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # l = 0
        
        s1Freq = {}
        for s in s1:
            s1Freq[s] = s1Freq.get(s,0) + 1
            
        
        windowFreq = {}
        windowSize = len(s1)
        for l in range(len(s2)):
            windowFreq.clear()
            windowFreq[s2[l]] = windowFreq.get(s2[l], 0) + 1
            if s2[l] not in s1Freq:
                continue
            r = 1
            while r < windowSize and l+r < len(s2):
                if s2[l+r] not in s1Freq:
                    break
                windowFreq[s2[l+r]] = windowFreq.get(s2[l+r], 0) + 1
                r+=1
            if windowFreq == s1Freq:
                return True    
            
        return False