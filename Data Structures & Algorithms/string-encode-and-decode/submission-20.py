DELIMITER = ">"

class Solution:
    # ["Hello","Magical","Wonderful","World"] -> "5>Hello7>Magical>9Wonderful5>World"
    def encode(self, strs: List[str]) -> str:        
        res = ""
        for s in strs:
            res += str(len(s)) + DELIMITER + s
        return res
    
    # "5>Hello7>Magical>9Wonderful5>World" -> ["Hello","Magical","Wonderful","World"]
    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        index = 0
        while index < len(s):
            lengthStringIndex = index
            while s[lengthStringIndex] != DELIMITER:
                lengthStringIndex += 1
            length = int(s[index:lengthStringIndex])
            index = lengthStringIndex + 1
            lengthStringIndex = index + length
            word = str(s[index:lengthStringIndex])
            res.append(word)
            index = lengthStringIndex
                
        return res