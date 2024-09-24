def issue_book(book_id, borrower_name):
    conn = connect_db()
    cursor = conn.cursor()

    # Check if the book is available
    cursor.execute("SELECT Quantity FROM Book WHERE BookID = ?", (book_id,))
    book = cursor.fetchone()
    
    if book and book[0] > 0:
        cursor.execute("""
        INSERT INTO IssuedBook (BookID, BorrowerName, IssueDate)
        VALUES (?, ?, GETDATE())
        """, (book_id, borrower_name))
        
        cursor.execute("""
        UPDATE Book SET Quantity = Quantity - 1 WHERE BookID = ?
        """, (book_id,))
        
        conn.commit()
        print("Book issued successfully!")
    else:
        print("Book is not available.")

    cursor.close()
    conn.close()

