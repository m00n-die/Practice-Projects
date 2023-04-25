# MD Logistics 
MD Logistics is a simple inventory management system built using python
Built to help my mom manage her business

# Documentation
* __init__(self, db_file): Initializes a connection to the database and creates the table if it does not exist.

* add_item(self, item_name, quantity, price): Adds an item to the inventory table with the given item_name, quantity, and price.

* remove_item(self, id): Removes an item from the inventory table with the given id.

* update_item(self, id, item_name=None, quantity=None, price=None): Updates the item in the inventory table with the given id. The item_name, quantity, and price arguments are optional and only the ones provided will be updated.

* view_all_items(self): Returns a list of all the items in the inventory table.

*search_item(self, item_name): Searches the inventory table for an item with the given item_name and returns a list of matching items.

# Contributions
Feel free to contribute to this project to make it better and more efficient
