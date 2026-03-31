DELIMITER = ";"

class Solution:
    # ["Hello","Magical","Wonderful","World"] -> "Hello;Magical;Wonderful;World"
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = ""
        for str in strs:
            result += str
            result += DELIMITER
        return result
        
    # "Hello;Magical;Wonderful;World" -> ["Hello","Magical","Wonderful","World"]
    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        result = [""]
        return_index = 0
        for c in s:
            if c == DELIMITER:
                return_index += 1
                result.append("")
                continue
            result[return_index] += c
        return result[0:-1]