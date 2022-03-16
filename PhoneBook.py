import sqlite3


def main():
    while True:
        print("""
        Main Menu
        1) View phone book
        2) Add to phone book
        3) Search for surname
        4) Delete person from phone book
        5) Quit`
        """)
        answer = int(input("Enter your selection:    "))
        if answer == 1:
            view_phone()
        elif answer == 2:
            add_phone()
        elif answer == 3:
            search_surname()
        elif answer == 4:
            delete_phone()
        elif answer == 5:
            print("Thank you")
            break
        else:
            print("Invalid option, please try again")


def view_phone():
    with sqlite3.connect("PhoneBook.db") as conn:
        cursor = conn.cursor()
        phone_list = cursor.execute("SELECT * FROM phone_book")
        for phone in phone_list.fetchall():
            print(phone)


def search_surname():
    surname_contact = input("please enter the surname of your contact:\n")
    with sqlite3.connect("PhoneBook.db") as conn:
        cursor = conn.cursor()
        phone_list = cursor.execute(
            "SELECT * FROM phone_book WHERE surname_contact=:surname_contact", {"surname_contact": surname_contact})
        for phone in phone_list.fetchall():
            print(phone)


def delete_phone():
    with sqlite3.connect("PhoneBook.db") as conn:
        cursor = conn.cursor()
        phone_list = cursor.execute("SELECT * FROM phone_book")
        for phone in phone_list.fetchall():
            print(phone)
    answer = int(input("Enter the ID of the row you'd like to delete"))
    with sqlite3.connect("PhoneBook.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM phone_book WHERE id_contact=:id_contact", {
                       "id_contact": answer})
        phone_list = cursor.execute("SELECT * FROM phone_book")
        for phone in phone_list.fetchall():
            print(phone)


def add_phone():
    while True:
        id_contact = int(input("Enter the id:           "))
        name_contact = input("Enter the First Name:  ")
        surname_contact = input("Enter the Surname:      ")
        phone_contact = int(input("Enter the phone number:    "))
        contact = (id_contact, name_contact,
                   surname_contact, phone_contact)
        with sqlite3.connect("PhoneBook.db") as conn:
            cursor = conn.cursor()
        cursor.execute("""INSERT INTO phone_book VALUES (:id_contact,:name_contact,:surname_contact,:phone_contact)""",
                       {"id_contact": id_contact, "name_contact": name_contact, "surname_contact": surname_contact, "phone_contact": phone_contact})
        conn.commit()
        new_contact = input("Would you  like to add a new contact? (y/n)")
        if new_contact == "n":
            break


main()
