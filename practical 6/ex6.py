# 6. Write a Python program to find common items from two lists

# defining the lists
list1=[1,2,3,4,5]
list2=[3,4,5,8,9]

# this is for storing common items in list
common=[]

# iteration list1
for item in list1:
    # if the same item is in list2
    if item in list2:
        # then append the item in common list
        common.append(item)

print(common)