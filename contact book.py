contacts = []

def add_contact():
    name = input("Enter Person Name: ")
    phone = input("Enter Mobile Number: ")
    email = input("Enter Email Address: ")
    address = input("Enter The Address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("contact book is Empty.\n")
    else:
        print("Contacts List:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
        print()

def search_contact():
    query = input("Enter Name or Phone Number to search: ")
    found = [c for c in contacts if query in (c['name'], c['phone'])]
    if found:
        for contact in found:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}\n")
    else:
        print("No matching contact found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'] == name:
            contact['phone'] = input("Enter New Phone Number: ")
            contact['email'] = input("Enter New Email: ")
            contact['address'] = input("Enter New Address: ")
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    global contacts
    contacts = [c for c in contacts if c['name'] != name]
    print("Contact deleted successfully!\n")

def main():
    while True:
        print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
