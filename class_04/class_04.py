# # IF 

# if <condition> :
#     operation 
# else :
#     operation 

num = 80
# simple if statement 
# if num < 40 :
#     print(f'{num} is less than 40')
# else :
#     print(f'{num} is more than 40')


# # nested if statement

# if <condition>:
#     if<condition>:
#         if<condition>:
#             operation 
#         else :
#             operation 
#     else :
#         operation
# else :
#     operation

# if <condition>:
#     operation
# elif <condition>:
#     operation
# else :
#     operation 

# num = 80
# if num < 40:
#     print(f'{num} is less than 40')
#     if num < 20:
#         print(f'{num} is less than 20')
#     else :
#         print(f'{num} is more than 20')
# else :
#     print(f'{num} in more then 40')
#     if num < 60:
#         print(f'{num} in less than 60')
#     else:
#         print(f'{num} is grater than 60')
#         print(num,'is grater than 60')
'''
x = 57

if x%2==0:
    print('even number')
else:
    print('odd number')
'''

# While 
#for
# match Case 
# comp 

# for i in range(5,10):
#     print(i)


num_list = [1,4,67,78,89,90]

num_tuple = (34,45,67,88,99)

num_set = {67,78,434,789,3453,353}

num_dict = {'a':56,'b':67,'c':98}

sum =0

# for i in num_dict.values():
#     print(i)

num = 1

# while num > 0 :
#     if num%2==0:
#         print(num**2)
#         num+=1
#     else:
#         print(num**3)
#         num+=1
# else:
#     print('number is greater than 10')
# list_3 = []
# num = 60


# match num:
#     case 60:
#         print('it is 0')
#         list_3.append(0)
#     case 10 | 30:
#         print('it is 10')
#         list_3.append(10)
#     case x if x>=40:
#         print('it greater than 40')
#         list_3.append(60)
     

# print(list_3)
    
num = [1,2,3,4,5]

sqr = [x**2 for x in num]

dict_1 = {x:x**2 for x in num}

print(sqr)
print(dict_1)

print(type(dict_1))