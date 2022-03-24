# 6. Write a program that takes the marks of 5 subjects and displays the grade

marathi = float(input("input marks for marathi : "))
science = float(input("input marks for science : "))
math = float(input("input marks for maths : "))
history = float(input("input marks for history : "))
geography = float(input("input marks for geography : "))

total = (marathi+science+math+history+geography)/5

if total>89:
    print("marks obtained",total," : Grade A")
elif total>69:
    print("marks obtained",total," : Grade B")
elif total>49:
    print("marks obtained",total," : Grade B")
elif total>36:
    print("marks obtained",total," : Grade B")
else:
    print("Fail")
