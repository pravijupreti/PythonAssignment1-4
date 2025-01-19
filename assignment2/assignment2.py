from assignment2.grocery_list import GroceryListManager  # Importing GroceryListManager

class Assignment2:
    def grocery_shop(self):
        manager = GroceryListManager()  # Create an instance of GroceryListManager
        
        while True:
            print("\nWould you like to")
            print("(1) Add")
            print("(2) Remove items")
            print("(3) Quit?")
            
            try:
                choice = int(input("Choose an option: "))
                if choice == 1:
                    manager.add_item()
                elif choice == 2:
                    manager.remove_item()
                elif choice == 3:
                    manager.show_list()
                    break
                else:
                    print("Incorrect selection.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

# Main entry point for the assignment2 module
if __name__ == "__main__":
    assignment = Assignment2()  # Create an instance of the assignment2 class
    assignment.grocery_shop()  # Start the grocery shopping process
