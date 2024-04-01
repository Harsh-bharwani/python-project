from datetime import datetime, timedelta

#catalog management
catalog=[{"Id":"Book 1 Id","title":"Book 1 title","author":"Book 1 author","quantity":3},
{"Id":"Book 2 Id","title":"Book 2 title","author":"Book 2 author","quantity":5},
{"Id":"Book 3 Id","title":"Book 3 title","author":"Book 3 author","quantity":7} ]

users={}
transactions={}

#function to display catalog
def display_catalog():
    print("Catalog Material: ")
    for books in catalog:
        print(books)

#function for user registration
def registration(user_id, name):
    users[user_id]={"name":name,"books_check_out":[]}

#function for books checkout
def checkout(user_id,book_id):
    if user_id not in users:
        print("Invalid user Id.")
        return
    if len(users[user_id]["books_check_out"])>3:
        print("You have exceeded maximum book withdrawing capacity at one time.")
        return
    for book in catalog:
        if book_id==book["Id"]:
            if book["quantity"]>0:
                 book["quantity"]-=1
                 users[user_id]["books_check_out"].append({ "id":book_id , "date":datetime.now()})
                 print("Book withdraw successfully.")
                 return
            else:
                 print("Book is unavailable.")
                 return
    print("Invalid book Id.")

# Function for book return
def return_book(user_id, book_id):
    if user_id not in users:
        print("Invalid user Id.")
        return
    for book in catalog:
        if book['Id'] == book_id:
            book['quantity'] += 1
            for transaction in users[user_id]["books_check_out"]:
                if transaction["id"] == book_id:
                    checkout_date = transaction["date"]
                    due_date = checkout_date + timedelta(days=14)
                    if datetime.now() > due_date:
                        days_overdue = (datetime.now() - due_date).days
                        fine = days_overdue * 1
                        print(f"Book returned successfully. Overdue fine: ${fine}")
                        users[user_id]["books_check_out"].remove(transaction)
                        return
                    else:
                        print("Book returned successfully.")
                        users[user_id]["books_check_out"].remove(transaction)
                        return
            print("You haven't checked out this book.")
            return
    print("Invalid Book ID.")

# Function to list overdue books for a user
def list_overdue_books(user_id):
    if user_id not in users:
        print("Invalid user Id.")
        return
    total_fine = 0
    print("Overdue Books:")
    for transaction in users[user_id]["books_check_out"]:
        book_id = transaction["id"]
        for book in catalog:
            if book['Id'] == book_id:
                checkout_date = transaction["date"]
                due_date = checkout_date + timedelta(days=14)
                if datetime.now() > due_date:
                    days_overdue = (datetime.now() - due_date).days
                    fine = days_overdue * 1
                    total_fine += fine
                    print(f"Book ID: {book_id}, Title: {book['title']}, Fine: ${fine}")
    print(f"Total Fine Due: ${total_fine}")

# Sample usage
registration("1", "Ram")
registration("2", "Shyam")

display_catalog()

checkout("1", "Book 1 Id")
checkout("1", "Book 2 Id")
checkout("2", "Book 1 Id")

return_book("1", "Book 1 Id")
return_book("1", "Book 2 Id")

list_overdue_books("1")