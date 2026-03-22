from personal_details_service import (
    create_person,
    read_people,
    update_person,
    delete_person
)

def show_people():
    rows = read_people()

    if not rows:
        print("No records found.")
        return

    for row in rows:
        print(f"ID: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}, Email: {row[3]}")


def main():
    while True:
        print("\nMenu")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            first_name = input("Enter first name: ").strip()
            last_name = input("Enter last name: ").strip()
            email = input("Enter email :").strip()
            create_person(first_name, last_name, email)

        elif choice == "2":
            show_people()

        elif choice == "3":
            person_id = int(input("Enter id to update: "))
            first_name = input("Enter new first name: ").strip()
            last_name = input("Enter new last name: ").strip()
            email = input("Enter new email: ").strip()
            update_person(person_id, first_name, last_name, email)

        elif choice == "4":
            person_id = int(input("Enter id to delete: "))
            delete_person(person_id)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

