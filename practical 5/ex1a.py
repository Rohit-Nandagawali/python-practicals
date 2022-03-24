# 1.Print the following patterns using loop:

# *
# **
# ***
# ****

for row in range(4):
    for col in range(row+1):
        print("*",end="")
    print()
    