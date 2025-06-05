def add_contacts(contacts):
    name=input("enter name to add:")
    mobile=int(input("enter mobile number:"))
    contacts[name]=mobile


def view_contacts(contacts):
    for i in contacts:
        print(f"{i}={contacts[i]}")


def edit_contact(contacts):
    name=input("enter name to change:")
    mobile=int(input("enter new number:"))
    contacts[name]=mobile
    print("after edit contact:" ,name)


def delete_contact(contacts):
    name=input("enter name to delete:")
    del contacts[name]
    print("deleted contact:",name)

def find_contact(contacts):
    name=input("enter name to find:")
    print(f"{name}= {contacts[name]}")

