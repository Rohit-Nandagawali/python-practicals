# 1. Write a Python program to sum all the items in a list.


# defining list
list1=[1,2,3]

# variable to store sum
sum=0
# loop will iterate each element in list1
for i in range(0,len(list1)):
    # add each element with sum
    sum=sum+list1[i]

# print the sum
print(sum)