from assignment3.Assignment3 import Assignment3
from Assignment1.string_test import StringTester
from assignment2.assignment2 import Assignment2
from assignment4.assignment4 import Assignment4

def main():
    assesment = int(input("Enter the assesment no:"))
    
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
