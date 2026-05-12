class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ageStart = 10 + 1
        
        res = 0

        for detail in details:
            if ord(detail[ageStart]) - ord('0') == 6:
                if ord(detail[ageStart+1]) - ord('0') >= 1:
                    res += 1
            elif ord(detail[ageStart]) - ord('0') > 6:
                res += 1

        return res 