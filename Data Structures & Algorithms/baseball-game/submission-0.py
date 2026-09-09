class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = [] 
        # res = 0 
        for i in range(len(operations)):
            if operations[i] == "+":
                stack.append(stack[-1] + stack[-2])
            elif operations[i] == "D":
                stack.append(stack[-1]*2)
            elif operations[i] == "C":
                stack.pop()
            else:
                stack.append(int(operations[i]))
        return sum(stack)





        #     stack.append(operations[i])

        # while len(stack)>=2:
        #     if operations[i] == "+":
        #         a = int(stack.pop())
        #         b = int(stack.pop())
        #         stack.append(a+b)
        # while stack:
        #     if operations[i] == "D":
        #         a = int(stack.pop())
        #         stack.append(a*2)
        #     if operations[i] == "C":
        #         stack.pop() 
        # return stack.sum()
            