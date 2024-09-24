def return_book(issue_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT BookID FROM IssuedBook WHERE IssueID = ?", (issue_id,))
    issued_book = cursor.fetchone()

    if issued_book:
        book_id = issued_book[0]

        cursor.execute("""
        UPDATE Book SET Quantity = Quantity + 1 WHERE BookID = ?
        """, (book_id,))
        
        cursor.execute("""
        DELETE FROM IssuedBook WHERE IssueID = ?
        """, (issue_id,))
        
        conn.commit()
        print("Book returned successfully!")
    else:
        print("Invalid issue ID.")

    cursor.close()
    conn.close()
