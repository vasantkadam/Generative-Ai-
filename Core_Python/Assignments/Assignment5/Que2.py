#2. Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students.

n=int(input("Enter the NUmber of Students:"))

for i in range(n):
    print(f"Student:{i+1}")
    total=0
    for j in range(5):
        marks =float(input("ENter the marks of subjects"))
        total+=marks
    percentage=total/5

    print(f"Total marks:,{total}")
    print(f"percentage:{percentage}")
