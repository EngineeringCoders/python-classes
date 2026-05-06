# create a variable 
x = 3.14

# airthematic operators 
# +, - , * , /, %, //(floor division), **(power)
a = 0 
b = 2

# sum 
add_result = a + b
print(f"the sum of {a} and {b} is {add_result}")

# subtraction 
sub_result = a - b
print(f"the difference of {a} and {b} is {sub_result}") 

# multiplication 
mul_result = a * b
print(f"the product of {a} and {b} is {mul_result}")

# division
quotient = a/b
print(f"the quotient {a} and {b} is {quotient}")

# remainder
remainder = a%b
print(f"the the division of {a} and {b} give remainder as {remainder} ")

# logical operators 
# 0 -> False 
# Any postive number -> True
# and , or , not
# and -> if and only if both of the operands are true than only the result will be true , else it will return false
condition_1 = a > 0 and b > 0
print(f"the result is : {condition_1}")
# or -> if any one of the operands is true than it will result in True
condition_2 = a > 0 or b > 0
print(f"the result is : {condition_2}")

# not -> inverse of given operand 
condition_3 = not a
print(f"the result is : {condition_3}")

x = 10
print(x > 5 and x < 20)

# assignment operators 
# =, +=, -=, *=, /=
# = -> assignment operator 
# += -> addition + assignment
# -= -> subtraction + assignment
# *= -> multiplication + assignment
# /= -> divsion + assigment 

# print(f"the value of x is {x}")
x += 10 # 10 + 10 -> x
# print(f"the value of x changed to {x}")
x -= 5
# print(f"the value of x after subtracting 5 changed to {x}")
x /=2
# print(f"the value of x changed to {x}")

# Bitwise Operator 
# &, ~, ^, <<, >>
a = 5 # 101
b = 3 # 011
# print(f"the result of bitwise and operation is {a & b}") 

# Membership operators => checks if something exists inside something
# in (present) , not in (not present)
# check if letter a is there in pradeep
print("a" in "pradeep")
print("i" not in "pradeep")

# Identity Operators => checks memory location , not just value
# is ( same object), is not (different object)
list_x = [1,2]
list_y = list_x.append(3)
print(f"location of list_x is {id(list_x)}")
print(f"location of list_y is {id(list_y)}")
print(list_x is list_y)
