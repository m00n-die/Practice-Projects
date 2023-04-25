import sqlite3

class Inventory:
    def __init__(self, db_file):
        """Initializes a connection to the database 
        and creates the table if it does not exist
        """
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS inventory (id INTEGER PRIMARY KEY, item_name TEXT, quantity INTEGER, price REAL)")
        self.conn.commit()

    def add_item(self, item_name, quantity, price):
        """Adds an item to the inventory table"""
        self.cur.execute("INSERT INTO inventory VALUES (NULL, ?, ?, ?)", (item_name, quantity, price))
        self.conn.commit()
        return "{} added successfully.".format(item_name)

    def remove_item(self, id):
        """Removes an item from the inventory table"""
        self.cur.execute("DELETE FROM inventory WHERE id=?", (id,))
        self.conn.commit()
        return "Item removed successfully."

    def update_item(self, id, item_name=None, quantity=None, price=None):
        """Updates the item in the inventory table
        arguments are optional and only the ones provided will be updated
        """
        if item_name:
            self.cur.execute("UPDATE inventory SET item_name=? WHERE id=?", (item_name, id))
        if quantity:
            self.cur.execute("UPDATE inventory SET quantity=? WHERE id=?", (quantity, id))
        if price:
            self.cur.execute("UPDATE inventory SET price=? WHERE id=?", (price, id))
        self.conn.commit()
        return "Item: {} updated successfully.".format(item_name)

    def view_all_items(self):
        """Returns a list of all the items in the inventory table"""
        self.cur.execute("SELECT * FROM inventory")
        rows = self.cur.fetchall()
        return rows

    def search_item(self, item_name):
        """Searches the inventory table for an item with the given 
        'item_name' and returns a list of matching items"""
        self.cur.execute("SELECT * FROM inventory WHERE item_name=?", (item_name,))
        rows = self.cur.fetchall()
        return rows


if __name__ == '__main__':
    db_file = "inventory.db"
    inventory = Inventory(db_file)

    while True:
        print("\nWelcome to the MD Logistics System\n")
        print("1. Add item")
        print("2. Update item")
        print("3. Delete item")
        print("4. View all items")
        print("5. Search")
        print("6. Exit")

        choice = input("Please enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            inventory.add_item(name, quantity, price)
            print("Item added successfully.")

        elif choice == '2':
            id = int(input("Enter item id: "))
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            inventory.update_item(id, name, quantity, price)
            print("Item updated successfully.")

        elif choice == '3':
            id = int(input("Enter item id: "))
            inventory.remove_item(id)
            print("Item deleted successfully.")

        elif choice == '4':
            items = inventory.view_all_items()
            if len(items) == 0:
                print("No items found.")
            else:
                print("ID    |      Name      |  Quantity  |  Price")
                print("------|----------------|------------|-------")
                for item in items:
                    print(f"{item[0]}     |  {item[1]}     |  {item[2]}       |  {item[3]}")

        elif choice == '5':
            name = str(input("Enter item name: "))
            inventory.search_item(name)

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")

    inventory.conn.close()
