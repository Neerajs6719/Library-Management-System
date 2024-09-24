def add_book(title, author, quantity):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(""" INSERT INTO Book (Title, Author, Quantity)
    VALUES (?,?,?)
    """, (title, author, quantity))
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Book added successfully!")
