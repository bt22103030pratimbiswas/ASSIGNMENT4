#program for grading systems
marks=int(input("Enter the marks of the student:"))
if marks<25:
    print("Grade obtained is F")
elif marks>=25 and marks<45:
    print("Grade obtained is E")
elif marks>=45 and marks<50:
    print("Grade obtained is D")
elif marks>=50 and marks<60:
    print("Grade obtained is C")
elif marks>=60 and marks<80:
    print("Grade obtained is B")
elif marks>=80:
    print("Grade obtained is A")
else:
    print("Student is failed in exam")