# 7. Write a Python program takes in a number and finds the sum of digits in a number

# 123 : 1+2+3=6
number = int(input("input a number : "))

sum = 0
remainder=0

while number > 0:
    remainder = number%10
    sum=sum+remainder
    number = number//10

print(sum)