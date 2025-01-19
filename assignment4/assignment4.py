# assignment4.py
from assignment4.sentence_operator import sentence_operator

class Assignment4:
    def sentence_Operator(self):
        # Create an instance of the sentence_operator class
        sentence_operator_instance = sentence_operator()

        # Taking user input for sentence
        sentence = input("Please enter sentence: ")
        
        # Split the sentence into words using space as a separator
        split_result = sentence_operator_instance.my_split(sentence, ' ')
        
        # Join the list back with commas and print the result
        joined_result = sentence_operator_instance.my_join(split_result, ',')
        
        # Displaying results
        print(joined_result)
        
        # Print each word in the split result
        for word in split_result:
            print(word)

if __name__ == "__main__":
    # Create an instance of Assignment4 class and call sentence_Operator
    assignment = Assignment4()
    assignment.sentence_Operator()
