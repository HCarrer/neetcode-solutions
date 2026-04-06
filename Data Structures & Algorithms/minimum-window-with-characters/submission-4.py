class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res, lenRes = [-1, -1], 1000

        l, r = 0, 0

        tOcur = {} # {X:1, Y:1, Z:1}
        windowOcur = {}
        for c in t:
            tOcur[c] = tOcur.get(c,0) + 1

        have, need = 0, len(tOcur)

        for r in range(len(s)):
            c = s[r]
            windowOcur[c] = windowOcur.get(c,0) + 1

            if c in tOcur and windowOcur[c] == tOcur[c]:
                have+=1

            while have == need:
                if (r-l+1) < lenRes:
                    res = [l, r]
                    lenRes = r-l+1

                windowOcur[s[l]] -= 1

                if s[l] in tOcur and windowOcur[s[l]] < tOcur[s[l]]:
                    have -= 1
                l+=1
        l,r = res


        return s[l : r+1] if lenRes != 1000 else ""