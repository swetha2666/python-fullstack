student={"name":"swetha","age":"20","marks":[98,96,95]}
print(student['name']) #accessing values
student['age']=19 # modifying values
student['city']='hyd'# adding new values
sum=0
for i in student['marks']:#calculate average and add to dictionary
    sum+=i
    student['avg']=sum/len(student['marks'])
for i in student: #print line by line dictionry values
    print(f"{i}={student[i]}")
print(student) 

