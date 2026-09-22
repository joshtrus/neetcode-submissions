import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+" : operator.add,
            "-" : operator.sub,
            "/" : lambda a, b: int(a / b),
            "*" : operator.mul
        }

        for token in tokens:
            if token in operators:
                a = stack.pop()
                b = stack.pop()
                res = operators[token](b, a)
                stack.append(res)
            else:
                stack.append(int(token))
        
        return stack[0]

        
        