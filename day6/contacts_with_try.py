#main code
import contacts_fun_try as fp
contacts={}
print("contact app")
try:
    while True:
        print("1.add contact")
        print("2.view contact")
        print("3.edit contact")
        print("4.delete contact")
        print("5. find contact")
        print("6.exit")
        choice=int(input("enter choice:"))
        if choice == 1:
            fp.add_contacts(contacts)
        elif choice == 2:
            fp.view_contacts(contacts)
        elif choice == 3:
            fp.edit_contact(contacts)
        elif choice == 4:
            fp.delete_contact(contacts)
        elif choice == 5:
            fp.find_contact(contacts)
        elif choice == 6:
            print("exit")
        else:
            print("end")
except Exception as error:
    print(f"error occured: {error}")
