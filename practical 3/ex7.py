# 7. Write a program to swap the value of two variables

num1 =  float(input("enter first number : "))
num2 =  float(input("enter second number : "))

# printing numbers before swapping
print("num1 = ",num1,", num2 = ",num2)

temp = num1
num1=num2
num2=temp

# printing numbers after swapping
print("num1 = ",num1,", num2 = ",num2)
