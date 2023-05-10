import sqlite3

class Users:
    def __init__(self, db_file):
        """Initializes a connection to the database 
        and creates the table if it does not exist
        """
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, user_name TEXT, user_pass TEXT)")
        self.conn.commit()
    
    def add_user(self, user_name, user_pass):
        """Adds a new user to the database"""
        self.cur.execute("INSERT INTO users VALUES (NULL, ?, ?)", (user_name, user_pass))
        self.conn.commit()
        return "{} successfully created.".format(user_name)
    
    def del_user(self, user_name):
        """Deletes a user from the database"""
        self.cur.execute("DELETE FROM users WHERE user_name=?", (user_name,))
        self.conn.commit()
        return "User {} successfully deleted.".format(user_name)
    
    def update_info(self, id, user_name=None, user_pass=None):
        """Updates a user's info in the dsatabase
        arguments are optional and only the ones provided will be updated
        """
        if user_name:
            self.cur.execute("UPDATE users SET user_name=? WHERE id=?", (user_name, id))
        if user_pass:
            self.cur.execute("UPDATE users SET user_pass=? WHERE id=?", (user_pass, id))
        self.conn.commit()
        return "User {} info updated".format(user_name)
    
    def view_all(self):
        """Returns a list of all users in the database"""
        self.cur.execute("SELECT * FROM users")
        rows = self.cur.fetchall()
        return rows
    
if __name__ == '__main__':
    db_file = "users.db"
    inventory = Users(db_file)

while True:
        print("\nWelcome to the Authentication System\n")
        print("1. Add User")
        print("2. Update User Info")
        print("3. Delete User")
        print("4. View all Users")
        print("5. Exit")

        choice = input("Please enter your choice (1-5): ")