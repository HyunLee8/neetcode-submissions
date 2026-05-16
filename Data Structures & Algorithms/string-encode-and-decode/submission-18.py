class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s

        return res

    def decode(self, s: str) -> List[str]:
        if len(s) is None:
            return []

        res = []

        i = 0
        snum = ""
        while i < len(s): 
            if s[i] != '#':
                snum += s[i]
                i += 1
            else:
                num = int(snum)
                string = s[i+1:i+1+num]
                res.append(string)
                i += num + 1
                snum = ""
        
        return res
