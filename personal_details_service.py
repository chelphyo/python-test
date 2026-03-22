from db import get_connection


def create_person(first_name, last_name, email):
    conn = None
    cur = None

    try: 
        conn = get_connection()
        cur = conn.cursor()

        query = """
        INSERT INTO employee.personal_details (first_name, last_name, email)
        VALUES (%s, %s, %s)
        """
        cur.execute(query, (first_name, last_name, email))
        conn.commit()
        print("Record created successfully.")

    except Exception as e:
        print("Error creating record:", e)
    finally:
        if cur:
            cur.close()
        if conn:
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

    cur.close()
    conn.close()

    return rows

def search_by_email(email):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        SELECT id, first_name, last_name, email
        FROM employee.personal_details
        WHERE email = %s
    """

    cur.execute(query, (email,))
    rows = cur.fetchall()

    cur.close()
    conn.close()
    return rows

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