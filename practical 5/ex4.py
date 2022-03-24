# 4. Write a Python program to print Fibonacci series.
# 0 1 1 2 3 5

a=0
b =1
print(a,end=" ")
print(b,end=" ")
for i in range(2,10):
    c=a+b
    a=b
    b=c
    print(c," ",end="")