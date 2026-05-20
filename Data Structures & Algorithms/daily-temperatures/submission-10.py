class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Naive solution: 

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
        '''
        
        # push k, v = {index, count} maybe and use monotonic s
        res = [None] *  len(temperatures)
        stack = []
        for i, n in enumerate(temperatures):
            if not stack or stack[-1][0] >= n:
                stack.append([n, i])
            else:
                while stack and stack[-1][0] < n:
                    res[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()

                stack.append([n, i])
        
        for i in range(len(res)):
            if res[i] is None:
                res[i] = 0
                
        return res

