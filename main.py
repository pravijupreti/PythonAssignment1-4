from assignment1.string_test import StringTester
from assignment2.assignment2 import Assignment2
from assignment4.assignment4 import Assignment4
from assignment3.assignment3 import Assignment3

def main():
    while True:
        try:
            # Prompt user for input and ensure it's an integer between 1 and 4
            assesment = int(input("Enter the assessment number (1-4): "))
            
            # Check if the input is within the valid range
            if assesment < 1 or assesment > 4:
                print("Invalid input. Please enter an integer between 1 and 4.")
                continue
            
            break  # Exit the loop if the input is valid
            
        except ValueError:
            # Handle the case where the input is not an integer
            print("Invalid input. Please enter a valid integer.")

    match assesment:
        case 3:
            # Create an instance of Assignment3 and call the method
            assignment3_instance = Assignment3()
            assignment3_instance.get_product()
        
        case 1:
            # Create an instance of StringTester and call the method
            string_tester_instance = StringTester()
            while True:
                user_input = input("Write something (quit ends): ")
                if user_input.lower() == "quit":
                    break
                string_tester_instance.tester(user_input)  # Call the method on the instance
        
        case 2:
            # Create an instance of assignment2 and call the method
            assignment2_instance = Assignment2()  # instance creation with 'self' support
            assignment2_instance.grocery_shop()  # Method call
        
        case 4:
            # Create an instance of Assignment4 and call the method
            assignment4_instance = Assignment4()
            assignment4_instance.sentence_Operator()

# Run the program
if __name__ == "__main__":
    main()
