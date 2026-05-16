class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            found = False
            for j in range(len(temperatures) - i - 1):
                if temperatures[j + i + 1] > temperatures[i]:
                    res.append(j + 1)
                    found = True
                    break
            if not found:
                res.append(0)
                
            print(res)
        
        return res