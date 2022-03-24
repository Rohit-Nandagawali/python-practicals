# 1010101
#  10101
#  101
#   1 

for row in range(7,0,-2):
    for spaces in range(6,row,-2):
        print(" ",end="")
    
    for col in range(1,row+1):
        print(col%2,end="")
    print()
