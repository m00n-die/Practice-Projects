import sqlite3

class Users:
    def __init__(self, db_file):
        """Initializes a connection to the database 
        and creates the table if it does not exist
        """
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, password TEXT, email TEXT)")
        self.conn.commit()
    
    def add_user(self, first_name, last_name, password, email):
        """Adds a new user to the database"""
        self.cur.execute("INSERT INTO users VALUES (NULL, ?, ?, ?, ?)", (first_name, last_name, password, email))
        self.conn.commit()
    
    def del_user(self, email):
        """Deletes a user from the database using the users email"""
        self.cur.execute("DELETE FROM users WHERE email=?", (email,))
        self.conn.commit()
    
    def update_info(self, id, first_name=None, last_name=None, password=None, email=None):
        """Updates a user's info in the dsatabase
        arguments are optional and only the ones provided will be updated
        """
        if first_name:
            self.cur.execute("UPDATE users SET first_name=? WHERE id=?", (first_name, id))
        if last_name:
            self.cur.execute("UPDATE users SET last_name=? WHERE id=?", (last_name, id))
        if password:
            self.cur.execute("UPDATE users SET password=? WHERE id=?", (password, id))
        if email:
            self.cur.execute("UPDATE users SET email=? WHERE id=?", (email, id))
        self.conn.commit()
    
    def view_all(self):
        """Returns a list of all users in the database"""
        self.cur.execute("SELECT * FROM users")
        rows = self.cur.fetchall()
        return rows
    
    def login(self, email, password):
        """logs in an exisiting user"""
        self.cur.execute("SELECT password FROM users WhERE email=?", (email,))
        key = self.cur.fetchall()
        password = [('{}'.format(password),)]
        if key != password:
            print("Invalid password. Try again")
        else:
            print("Login success")
        self.conn.commit()
        
if __name__ == '__main__':
    db_file = "users.db"
    users = Users(db_file)

    while True:
            print("\nWelcome to the User Management System\n")
            print("1. Add User")
            print("2. Update User Info")
            print("3. Delete User")
            print("4. View all Users")
            print("5. Login")
            print("6. Exit")

            choice = input("Please enter your choice (1-6): ")

            if choice == '1':
                first_name = input("Enter your first name: ")
                last_name = input("ENter your last name: ")
                password = input("Enter your password: ")
                email = input("Enter your email: ")
                users.add_user(first_name, last_name, password, email)
                print("Your account has been successfully created!")

            elif choice == '2':
                first_name = input("Enter your first name: ")
                last_name = input("ENter your last name: ")
                password = input("Enter your password: ")
                email = input("Enter your email: ")
                users.update_info(first_name, last_name, password, email)
                print("Info successfully updated")

            elif choice == '3':
                name = input("Enter the email of the account you wish to delete: ")
                users.del_user(name)
                print("User deleted")

            elif choice == '4':
                items = users.view_all()
                if len(items) == 0:
                    print("No registered users in the database.")
                else:
                    print("ID    |      First Name          |       Last Name")
                    print("------|--------------------------|----------------")
                    for item in items:
                        print(f"{item[0]}     |  {item[1]}                    |  {item[2]}")

            elif choice == '5':
                email = input("Enter your account email: ")
                password = input("Enter your account password: ")
                users.login(email, password)
                
            elif choice == '6':
                break

            else:
                print("Invalid choice. Please try again.")

    users.conn.close()