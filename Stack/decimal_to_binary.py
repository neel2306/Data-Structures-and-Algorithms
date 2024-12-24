'''
Idea is to use stack to convert a decimal number to binary
'''

from Stack import Stack

def converter(num: int) -> str:
    # Instantiate stack class
    s = Stack()

    while num > 0:
        remainder = num % 2
        s.push(remainder)
        num //= 2
    
    binary = ''
    while not s.isEmpty():
        binary = binary + str(s.pop())
    
    return binary

""" print(converter(45)) # 101101 """