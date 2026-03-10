# List Comprehensation : is a short and efficient way to create a list using single line of code with a loop and condition

# Syntax :: new_list=[expression for item in iterable ]

# 1. square

# lst=[]

# n=int(input("Enter number of elements range :: "))

# for i in range(n):
#     lst.append(int(input("Enter Element :: ")))

# #single line logic
# square=[num*num for num in lst]

# print("Original List :: ",lst)
# print("Square list is :: ",square)

# ======================================================================

# # 2. Cube 
# lst=[]

# n=int(input("Enter number of elements range :: "))

# for i in range(n):
#     lst.append(int(input("Enter Element :: ")))


# cube=[num**3 for num in lst]

# print("Cube : ",cube)

# ======================================================================

# # 3. Even numbers from list 
# lst=[]

# n=int(input("Enter number of elements range :: "))

# for i in range(n):
#     lst.append(int(input("Enter Element :: ")))

# even=[num for num in lst if num%2==0]

# print("Even numbers From list :: ",even)

# ======================================================================

# # 4. Odd numbers from list 
# lst=[]

# n=int(input("Enter number of elements range :: "))

# for i in range(n):
#     lst.append(int(input("Enter Element :: ")))

# odd=[num for num in lst if num%2!=0]

# print("Even numbers From list :: ",odd)

# ======================================================================

# # 5. convert list in string 

# lst=[]

# n=int(input("Enter number of elements range :: "))

# for i in range(n):
#     lst.append(int(input("Enter Element :: ")))

# str_list=[str(num) for num in lst]

# print("String list is :: ",str_list)


# ======================================================================
# 6. Square of only even number

lst=[]

n=int(input("Enter number of elements range :: "))

for i in range(n):
    lst.append(int(input("Enter Element :: ")))

even=[num*num for num in lst if num%2==0]

print("Square of Even numbers From list :: ",even)
