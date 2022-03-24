# 4. Write a program to check if the input year is a leap year of not
from email.policy import default


year = int(input("input year  : "))

if year%4==0 or year%100==0 or year%400==0:
    print(year,"is a leap year")

else : print(year,"is not a leap year")