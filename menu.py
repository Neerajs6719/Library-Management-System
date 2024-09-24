def menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View Available Books")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            quantity = int(input("Enter quantity: "))
            add_book(title, author, quantity)
        
        elif choice == '2':
            book_id = int(input("Enter book ID: "))
            borrower_name = input("Enter borrower's name: ")
            issue_book(book_id, borrower_name)

        elif choice == '3':
            issue_id = int(input("Enter issue ID: "))
            return_book(issue_id)

        elif choice == '4':
            view_books()

        elif choice == '5':
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    menu()
