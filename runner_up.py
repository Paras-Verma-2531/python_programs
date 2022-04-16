number_of_student=int(input("enter the number of students: "))
marks=[]
for i in range(number_of_student):
    score=int(input(f"enter the marks of {i+1} student: "))
    marks.append(score)
marks.sort()
marks1=[]
for  i in range(len(marks)):
    if  marks[i] in marks1:
        continue
    else:
        marks1.append(marks[i])
print(f"the runner's up score is {marks1[len(marks1)-2]}") 
       