# Write a program to convert bits to Megabytes, Gigabytes and Terabytes

bit = float(input("Enter bit\n"))


# 1 bit  = 1.25x10**-7 Megabytes
megabyte = bit*1.25*10**-7

# 1 bit = 1.25x10**-10 Gigabytes
gigabyte = bit*1.25*10**-10

#1 bit = 1.25x10**-13 Terabyte
terabyte = bit*1.25*10**-13

# printing

print(bit," bit/bits = ",megabyte," MB")
print(bit," bit/bits = ",gigabyte," GB")
print(bit," bit/bits = ",terabyte," TB")
