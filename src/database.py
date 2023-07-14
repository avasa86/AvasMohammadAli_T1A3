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

        # Create the second table with a foreign key reference to the subject table
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
        c.execute("INSERT INTO subject (subject_name) VALUES (?)",(subject_name,))

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


def update_student(first_name,last_name,email,age,phone_number,parents_phone_number,mark,subject_id,ids):
    # Connect to the SQLite database
    conn = sqlite3.connect('studentdatabase.db')
    c = conn.cursor()

    try:
        # Update the student
        c.execute("UPDATE student SET first_name = ?,last_name = ?,email = ?,age = ?,phone_number = ?,parents_phone_number = ?,mark = ?,subject_id = ? WHERE id = ?", (first_name,last_name,email,age,phone_number,parents_phone_number,mark,subject_id,ids))

        # Commit the changes
        conn.commit()
        print("Student updated successfully!")

    except sqlite3.Error as e:
        print("Error updating student details:", e)

    finally:
        # Close the connection
        conn.close()




def update_subject(subject_name,subject_id):
    # Connect to the SQLite database
    conn = sqlite3.connect('studentdatabase.db')
    c = conn.cursor()

    try:
        # Update the subject
        c.execute("UPDATE subject SET subject_name = ? WHERE id = ?", (subject_name,subject_id))

        # Commit the changes
        conn.commit()
        print("Subject updated successfully!")

    except sqlite3.Error as e:
        print("Error updating subject name:", e)

    finally:
        # Close the connection
        conn.close()


def delete_student(record_id):
    # Connect to the SQLite database
    conn = sqlite3.connect('studentdatabase.db')
    c = conn.cursor()

    try:
        # Delete the record from the table
        c.execute("DELETE FROM student WHERE id = ?", (record_id))

        # Commit the changes
        conn.commit()
        print("Record deleted successfully!")

    except sqlite3.Error as e:
        print("Error deleting record:", e)

    finally:
        # Close the connection
        conn.close()    

def delete_subject():
    # Connect to the SQLite database
    conn = sqlite3.connect('studentdatabase.db')
    c = conn.cursor()

    try:
        # Delete the student from the table
        c.execute("DELETE FROM subject WHERE subject_name = ?", (subject_name,))

        # Commit the changes
        conn.commit()
        print("Record deleted successfully!")

    except sqlite3.Error as e:
        print("Error deleting record:", e)

    finally:
        # Close the connection
        conn.close()    
  

create_table()
insert_subject('Maths')
insert_subject('Physics')
insert_subject('Chemistry')
insert_subject('Economics')
insert_student("Avas","Ali","aa@gmail.com",29,"0444444444","0455551255",98,1)
insert_student("Aban","Bad","ab@gmail.com",30,"04445986","0455555235",95,2)
insert_student("Cat","Dinoson","ac@gmail.com",35,"0444442344","0445555555",93,3)
insert_student("Aprer","Aci","ad@gmail.com",36,"0445644444","0458955555",91,4)
update_student("Aprer","Aci","ad@gmail.com",36,"0445644444","0458955555",69,1,4)
update_subject('Geography',2)

