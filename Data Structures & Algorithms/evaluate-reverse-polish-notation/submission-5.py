class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c not in ["*", "/", "+", "-"]:
                stack.append(c)
            # while len(stack) >= 2 :
            if c == "+":
                a = int(stack.pop()) 
                b = int(stack.pop())
                item = a+b
                stack.append(item)
            if c == "-":
                a = int(stack.pop()) 
                b = int(stack.pop())
                item = b-a
                stack.append(item)
            if c == "*":
                a = int(stack.pop()) 
                b = int(stack.pop())
                item = a*b
                stack.append(item)
            if c == "/":
                a = int(stack.pop()) 
                b = int(stack.pop())
                item = b/a
                stack.append(item)
           
        return int(stack.pop())
