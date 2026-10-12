class Solution:
    def isValid(self, s: str) -> bool:
        #clarifying Questions and Assumptions


        #Possible Solution


        #Better Solution

        stack = []
        opener = ["(", "[", "{"]

        if len(s) == 0:
            return True 
        
        for ch in s:
            if ch in opener:
                stack.append(ch)
            
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()

                if ((top == "(" and ch != ")") or(top == "[" and ch != "]") or(top == "{" and ch != "}")):
                    return False
        
        return len(stack) == 0
