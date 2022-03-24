# 8. Write a Python program that takes a number and checks whether it is a palindrome or not.

# 121 = 121 
# reverse number is also same as original



number = int(input("input a number : "))

original_num = number

reverse =0
remainder =0

while number>0:
    remainder = number % 10
    reverse =( reverse*10)+remainder
    number//=10

if reverse == original_num:
    print("number is palindrome")

else:
    print("number is not palindrome")


