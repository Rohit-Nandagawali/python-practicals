# 5. Write a Python program to calculate factorial of a number

# 5!=120 : 1x2x3x4x5

number= int(input("input number : "))

result = 1

for i in range(1,number+1):
    result = result*i

print("factorial of a given number is ",result)