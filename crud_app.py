import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="firstdb",
        user="postgres",
        password="Master@123"
    )

def create_person(first_name, last_name, email):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        INSERT INTO employee.personal_details (first_name, last_name, email)
        VALUES (%s, %s, %s)
    """
    cur.execute(query, (first_name, last_name, email))
    conn.commit()

    cur.close()
    conn.close()
    print("Record created successfully.")

    cur.close()
    conn.close()

def read_people():
    conn = get_connection()
    cur = conn.cursor()

    query = """
        SELECT id, first_name, last_name, email
        FROM employee.personal_details
        ORDER BY id
    """
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def update_person(person_id, first_name, last_name, email):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        UPDATE employee.personal_details
        SET first_name = %s, last_name = %s, email = %s
        WHERE id = %s
    """
    cur.execute(query, (first_name, last_name, email, person_id))
    conn.commit()

    cur.close()
    conn.close()
    print("Record updated successfully.")

def delete_person(person_id):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        DELETE FROM employee.personal_details
        WHERE id = %s
    """
    cur.execute(query, (person_id,))
    conn.commit()

    cur.close()
    conn.close()
    print("Record deleted successfully.")

if __name__ == "__main__":
    while True:
        print("\nMenu")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email :")
            create_person(first_name, last_name, email)

        elif choice == "2":
            read_people()

        elif choice == "3":
            person_id = int(input("Enter id to update: "))
            first_name = input("Enter new first name: ")
            last_name = input("Enter new last name: ")
            email = input("Enter new email: ")
            update_person(person_id, first_name, last_name, email)

        elif choice == "4":
            person_id = int(input("Enter id to delete: "))
            delete_person(person_id)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

