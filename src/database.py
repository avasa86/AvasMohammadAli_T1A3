import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('studentdatabase.db')
c = conn.cursor()

def create_table():
    try:
        # Create the first table
        c.execute('''CREATE TABLE subject (
                        id INTEGER PRIMARY KEY,
                        subject_name TEXT
                    )''')

        # Create the second table with a foreign key reference to the customers table
        c.execute('''CREATE TABLE student (
                        id INTEGER PRIMARY KEY,
                        first_name TEXT,
                        last_name TEXT,
                        email TEXT,
                        age INTEGER,
                        phone_number TEXT,
                        parents_phone_number TEXT,
                        mark INTEGER,
                        subject_id INTEGER,
                        FOREIGN KEY (subject_id) REFERENCES subject(id)
                    )''')

        # Commit the changes and close the connection
        conn.commit()
        print("Table Successfully Created")

    except sqlite3.Error as e:
        print("Error creating table",e)

    finally:
        conn.close()



def insert_subject(subject_name):
    # Connect to the SQLite database
    conn = sqlite3.connect('studentdatabase.db')
    c = conn.cursor()

    try:
        # Insert the contact into the table
        c.execute("INSERT INTO subject (subject_name) VALUES (?)",(subject_name))

        # Commit the changes
        conn.commit()
        print("Subject inserted successfully!")

    except sqlite3.Error as e:
        print("Error inserting contact:", e)

    finally:
        # Close the connection
        conn.close()

def insert_student(first_name,last_name,email,age,phone_number,parents_phone_number,mark,subject_id):
    # Connect to the SQLite database
    conn = sqlite3.connect('studentdatabase.db')
    c = conn.cursor()

    try:
        # Insert the contact into the table
        c.execute("INSERT INTO student (first_name,last_name,email,age,phone_number,parents_phone_number,mark,subject_id) VALUES (?,?,?,?,?,?,?,?)",(first_name,last_name,email,age,phone_number,parents_phone_number,mark,subject_id))

        # Commit the changes
        conn.commit()
        print("Student inserted successfully!")

    except sqlite3.Error as e:
        print("Error inserting contact:", e)

    finally:
        # Close the connection
        conn.close()


create_table()
insert_subject('Maths')
insert_subject('Physics')
insert_student("Avas","Ali","aa@gmail.com",29,"0444444444","0455555555",98,1)

