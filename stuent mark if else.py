students=["ram","tom","jack"]
marks=[55,70,49]
passing_students=[]
fail=0
for i in range(len(students)):
    if marks[i]>=50:
        passing_students.append(students[i]+":"+str(marks[i]))
    else:
        fail+=1
        print("passing student",passing_students)
        print("fail",fail)       