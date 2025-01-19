Assignment Program
This is a Python-based program that allows users to interact with different assignments (1-4) based on their selection. Each assignment is designed to solve a particular problem using a variety of programming concepts like string manipulation, lists, and exception handling.

Table of Contents
Overview
Assignments
Installation
Usage
Contributing
License
Overview
This repository contains multiple assignments that are built and organized as separate modules. Users can choose the assignment they wish to execute by entering an integer corresponding to the assignment number. Each assignment has its own functionality:

Assignment 1: String manipulation with a default value checker.
Assignment 2: Grocery list management system (add/remove items).
Assignment 3: Product retrieval (mock-up).
Assignment 4: Sentence manipulation with specific operations.
The user is asked to choose the assignment they want to work with, and the corresponding program will run. The program includes error handling and input validation for a smooth user experience.

Assignments
Assignment 1: String Tester
In this assignment, the user is prompted to enter a string. If the string length is less than 10 characters, a default message "Too short" is printed. If the string length is greater than or equal to 10 characters, the string entered by the user is printed.

Key Concepts: Default arguments, String length validation.
Assignment 2: Grocery List Management
This assignment allows the user to manage a grocery shopping list by adding, removing, and displaying items. The user can:

Add items to the grocery list.

Remove items by specifying their index.

View the current grocery list before quitting.

Key Concepts: List operations, input validation, user interaction.

Assignment 3: Product Retrieval
This assignment prompts the user to retrieve product details. It provides an interactive way to search for products and displays relevant information.

Key Concepts: Object-oriented programming, product management.
Assignment 4: Sentence Manipulation
This assignment performs operations on sentences, where the user can apply certain predefined operations (like uppercase conversion, word removal, etc.) to manipulate sentences.

Key Concepts: String operations, list operations.
Installation
To run this program locally, you need to have Python installed. Follow these steps to set it up:

Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/assignment-program.git
Navigate to the project folder:

bash
Copy
Edit
cd assignment-program
Create a virtual environment (recommended):

bash
Copy
Edit
python3 -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy
Edit
venv\Scripts\activate
On macOS/Linux:
bash
Copy
Edit
source venv/bin/activate
Install required dependencies (if any):

bash
Copy
Edit
pip install -r requirements.txt
Usage
Once the environment is set up, run the program using:

bash
Copy
Edit
python main.py
You will be prompted to enter the assignment number (1-4) and interact with the program as per the assignment.

