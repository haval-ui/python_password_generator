student_hights=input("enter the students hights: ").split()

for n in range(0,len(student_hights)):
    student_hights[n]=int(student_hights[n])

number_of_students=0
hight_sum=0
for i in student_hights:
     hight_sum+=i
     number_of_students+=1
avg=hight_sum/number_of_students
print(f"the average hight is: {avg} ")  