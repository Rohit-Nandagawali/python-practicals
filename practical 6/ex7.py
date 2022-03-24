# 7. Write a Python program to select the even items of a list.

# defining the lists
list1=[1,2,3,4,5]

# for storing even numbers
even=[]

# traversing list
for item in list1:
    # if item is even then
    if item%2==0:
        #then append in list 
        even.append(item)

# printing even 
print(even)