class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openers = ["(", "[", "{"]


        for c in s:
            if c in openers:
                stack.append(c)
            else:
                if not stack:
                    return False 
                    
                stack_top = stack.pop()

                if( stack_top == "(" and c != ")" 
                or stack_top == "[" and c != "]" 
                or stack_top == "{" and c != "}" ):
                    return False
        
        return True if not stack else False
        
        