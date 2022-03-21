# 150. Evaluate Reverse Polish Notation 
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+", "-", "/", "*"]
        for token in tokens:
            if token in ops:
                op2, op1 = int(stack.pop()), int(stack.pop())
                if token == "+":
                    stack.append(op1 + op2)
                if token == "-":
                    stack.append(op1 - op2)
                if token == "/":
                    stack.append(int(op1 / op2))
                if token == "*":
                    stack.append(op1 * op2)
            else:
                stack.append(token)
        return stack.pop()
