def evaluate_postfix(expression):
    stack = []
    
    for token in expression.split():
        if token.lstrip('-').isdigit():  # check if token is an integer
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))
    
    return stack[0]

expression = input("Enter postfix expression: ")
result = evaluate_postfix(expression)
print("Result:", result)