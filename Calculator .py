def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Invalid operator"

# --- How to use it ---
print(calculate(10, '+', 5))  
print(calculate(20, '*', 3)) 
print(calculate(8, '/', 0))   
