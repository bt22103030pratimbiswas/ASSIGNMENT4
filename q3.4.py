import random
num_of_questions=11
points=0
for i in range(1,num_of_questions):
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    ans=int(input("Question {}: {}*{}=".format(i,num1,num2)))
    if ans==num1*num2:
        print("Right!")
        points+=1
    else:
        print("Wrong.The correct answer is {}".format(num1*num2))
    print("Number of points obtained is {}".format(points))
    print("You scored",points)