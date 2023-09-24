subjects = int(input("Enter the number of subjects: "))
marks = {}
for i in range(subjects):
    subject = input("Enter the subject name: ")
    mark = int(input(f"Enter the marks for {subject}: "))
    marks[subject] = mark
total_marks = sum(marks.values()) #.values()method returns view object...the view obj contains the values of dictionary ,as like list...
average_marks = total_marks / subjects
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
failed_subjects = []
for subject, mark in marks.items():  #.items() nested tuple
    if mark < 50:
        failed_subjects.append(subject)
        if len(failed_subjects) > 0:
    print("Failed Subjects:")
    for subject in failed_subjects:
        print(subject)else:
    print("CongratulationsYou passed all subjects!")

