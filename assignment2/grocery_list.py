class GroceryListManager:
    def __init__(self):
        self.grocery_list = []

    def add_item(self):
        item = input("What will be added?: ").strip()
        self.grocery_list.append(item)
        print(f'"{item}" has been added to the list.')

    def remove_item(self):
        if not self.grocery_list:
            print("The list is empty. Nothing to remove.")
            return

        print(f"There are {len(self.grocery_list)} items in the list.")
        try:
            item_index = int(input("Which item is deleted?: "))
            if 0 <= item_index < len(self.grocery_list):
                removed_item = self.grocery_list.pop(item_index)
                print(f'"{removed_item}" has been removed from the list.')
            else:
                print("Incorrect selection.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def show_list(self):
        if not self.grocery_list:
            print("The list is empty.")
        else:
            print("The following items remain in the list:")
            for item in self.grocery_list:
                print(item)
