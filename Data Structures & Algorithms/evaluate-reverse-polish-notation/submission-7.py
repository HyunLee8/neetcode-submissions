class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            print(stack)
            if len(t) > 1 or t.isalnum():
                stack.append(int(t))
            else:
                second = stack.pop()
                first = stack.pop()
                a = 0

                if t == '+':
                    a = first + second
                elif t == '-':
                    a = first - second
                elif t == '*':
                    a = first * second
                elif t == '/':
                    a = first / second
            
                stack.append(int(a))
        
        return stack.pop()