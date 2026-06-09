'''
operator 

operators are used to perform operations on variables and values.

Python divides the operators in the following groups:
1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators
5. Identity operators
6. Membership operators
7. Bitwise operators
'''

#arithmetic operators
'''Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.'''
a = 10
b = 3
print(a + b) # addition
print(a - b) # subtraction
print(a * b) # multiplication
print(a / b) # division
print(a % b) # modulus
print(a ** b) # exponentiation
print(a // b) # floor division

#assignment operators
'''Assignment operators are used to assign values to variables.'''
a = 10
a += 5 # a = a + 5
print(a)
a -= 5 # a = a - 5
print(a)
a *= 5 # a = a * 5
print(a)
a /= 5 # a = a / 5
print(a)
a %= 5 # a = a % 5
print(a)
a **= 5 # a = a ** 5
print(a)
a //= 5 # a = a // 5
print(a)    

#comparison operators
'''Comparison operators are used to compare two values.'''
a = 10
b = 3
print(a == b) # equal to
print(a != b) # not equal to
print(a > b) # greater than
print(a < b) # less than
print(a >= b) # greater than or equal to
print(a <= b) # less than or equal to

#logical operators
'''Logical operators are used to combine conditional statements.'''
a = True
b = False
print(a and b) # logical AND
print(a or b) # logical OR
print(not a) # logical NOT

#identity operators
'''Identity operators are used to compare the memory locations of two objects.'''
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) # False
print(a is not b) # True        

#membership operators
'''Membership operators are used to test if a sequence is presented in an object.'''
a = [1, 2, 3]
print(1 in a) # True
print(4 in a) # False
print(1 not in a) # False
print(4 not in a) # True    

#bitwise operators
'''Bitwise operators are used to perform bitwise operations on integers.'''
a = 10 # 1010 in binary
b = 3 # 0011 in binary
print(a & b) # bitwise AND
print(a | b) # bitwise OR
print(a ^ b) # bitwise XOR
print(~a) # bitwise NOT
print(a << 1) # bitwise left shift
print(a >> 1) # bitwise right shift 

#tpe of operators
'''There are three types of operators in Python:
1. Unary operators: Operators that operate on a single operand. Example: -a, +a, not a
2. Binary operators: Operators that operate on two operands. Example: a + b, a - b, a * b, a / b
3. Ternary operators: Operators that operate on three operands. Example: a if condition else b'''

#operator precedence
'''Operator precedence determines the order in which operators are evaluated in an expression.'''
a = 10
b = 3
c = 5
print(a + b * c) # 10 + (3 * 5) = 25
print((a + b) * c) # (10 + 3) * 5 = 65
print(a + b / c) # 10 + (3 / 5) = 10.6
print((a + b) / c) # (10 + 3) / 5 = 2.6

#operator associativity
'''Operator associativity determines the order in which operators of the same precedence are evaluated in an expression.'''
a = 10
b = 3
c = 5
print(a - b - c) # (10 - 3) - 5 = 2
print(a - (b - c)) # 10 - (3 - 5) = 12
print(a / b / c) # (10 / 3) /
print(a / (b / c)) # 10 / (3 / 5) = 16.666666666666668  

