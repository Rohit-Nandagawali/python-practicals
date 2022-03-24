# 6. Write a program to calculate surface volume and area of a cylinder.


PIE = 3.14 
radius = float(input("input radius of cyclinder : "))
height = float(input("input height of cyclinder : "))

area = 2*PIE*radius*(radius+height)
volume =  2*PIE*radius**2

print("Surface volume of cylinder : ",area)
print("Surface area of cylinder : ",volume)
