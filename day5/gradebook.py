#main part
import gradebook_fun as gf
gradebook = {}
print("student gradebook")
while True:
    print("1.Add students along with their marks for multiple subjects.")
    print("2.View all students and their marks with average scores.")
    print("3.Search for a student by name.")
    print("4.Update marks of an existing student.")
    print("5.Remove a student from the gradebook.")
    print("6.Exit the program when done.")
    choice=int(input("enter choice:"))
    if choice==1:
        gf.add_student(gradebook)
    elif choice == 2:
        gf.view_student(gradebook)
    elif choice == 3:
        gf.search_student(gradebook)
    elif choice == 4:
        gf.update_student(gradebook)
    elif choice == 5:
        gf.remove_student(gradebook)
    elif choice == 6:
        print("exit")
    else:
        print("invalid choice...")
    

        



