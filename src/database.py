import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('studentdatabase.db')
c = conn.cursor()

# Create the first table
c.execute('''CREATE TABLE subject (
                id INTEGER PRIMARY KEY,
                name TEXT,
            )''')

# Create the second table with a foreign key reference to the customers table
c.execute('''CREATE TABLE student (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                email TEXT,
                age INTEGER,
                phone_number TEXT,
                parents_phone_number TEXT
                subject_id INTEGER,
                mark INTEGER,
                FOREIGN KEY (subject_id) REFERENCES subject(id)
            )''')

# Commit the changes and close the connection
conn.commit()
conn.close()