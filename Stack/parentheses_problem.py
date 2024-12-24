'''
Basically we want to see if the parentheses provided are right or not.
'''

from Stack import Stack

mapper = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    ')' : '(',
    ']' : '[',
    '}' : '{'
}

def parentheses_checker(equation: str) -> None:
    
    # Instantiate stack element
    s: Stack = Stack()

    checker: bool = True

    # Loop over the string to find parentheses
    for element in range(len(equation)):

        if equation[element] in '([{':
            s.push(element = equation[element])
        
        else:
            if s.isEmpty():
                checker = False
            
            else:
                top = s.pop()
                if not top == mapper[equation[element]]:
                    checker = False
    if checker and s.isEmpty():
        return True
    
    else:
        return False

""" equation = str(input("Enter the equation: "))
answer = parentheses_checker(equation=equation)
print(answer) """