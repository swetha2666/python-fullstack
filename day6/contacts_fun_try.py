def add_contacts(contacts):
    try:
        name=input("enter name to add:")
        mobile=int(input("enter mobile number:"))
        file=open("contacts_try.txt","a")
        file.write(f"{name},{mobile}")
    except Exception as error:
        print("error occured{error}")




def view_contacts(contacts):
    try:
        file=open("contacts_try.txt","r")
        contacts=file.read()
        print(contacts)
        # for i in contacts:
        #     print(f"{i}={contacts[i]}")
    except Exception as error:
        print(f"no contacts{error}")


def edit_contact(contacts):
    try:
        file=open("contacts_try.txt","r+")
        contacts=file.write(f"{name},{mobile}")
        name=input("enter number to change:")
        mobile=int(input("enter new number:"))
        x=contacts[name]=mobile
        print("after editing :{x}")
    except Exception as error:
          print(f"nothing to edit!!{error}")




def delete_contact(contacts):
    try:
        file=open("contacts_try.txt","r+")
        name=input("enter name to delete:")
        if name in contacts_try.txt:

           data=file.write()
           del contacts_try.txt[name] 
        print(f"deleted contact:,{name}")
    except Exception as error:
        print(f"nothing to delete:{error}")
    

# def find_contact(contacts):
#     name=input("enter name to find:")
#     print(f"{name}= {contacts[name]}")

