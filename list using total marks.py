num_subjects = int(input("Enter the number of subjects: "))
marks = [ ]
for i in range(num_subjects):
    subject_mark = float(input(f"Enter the marks for subject {i+1}: "))
    marks.append(subject_mark)
total_marks = sum(marks)
average_marks = total_marks / num_subjects

print("Total marks:", total_marks)
print("Average marks:", average_marks)
if average_marks > 70:
    print("Grade: First Class")
elif average_marks > 60:
    print("Grade: Second Class")
elif average_marks >= 50:
    print("Grade: Third Class")
else:
    print("Grade: Fail")


