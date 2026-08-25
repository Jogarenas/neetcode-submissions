class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string))
            encoded += "#"
            
            
            for char in string:
                encoded += char
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        
        final = []
        strlen = ""
        pos = 0
        jump = 0
        while pos < len(s):
            if s[pos] == "#":
                jump = int(strlen)
                final.append(s[pos + 1: pos + 1 + jump])
                pos += jump + 1
                strlen = ""
            if pos < len(s):
                strlen += s[pos]
                pos += 1

        return final


            