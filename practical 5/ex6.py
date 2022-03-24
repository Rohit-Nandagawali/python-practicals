# 6. Write a Python Program to Reverse a Given Number

# 123 = 321


number = int(input("input a number : "))

sum = 0
remainder=0

while number > 0:
    remainder = number%10
    sum=(sum*10)+remainder
    number = number//10

print(sum)