# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.

def main():

    with open("questions.txt", 'r') as file_handle:
        while True:
            # reads the question
            question = file_handle.readline().strip()
            # .readline() reads one line from the file
            # .strip() removes any leading or trailing whitespace, including spaces, tabs, and newline characters
            if not question:  # Check if the question is empty (end of file)
                break

            # Read the answer choices
            # and remove any extra whitespace
            answer1 = file_handle.readline().strip()
            answer2 = file_handle.readline().strip()
            answer3 = file_handle.readline().strip()
            answer4 = file_handle.readline().strip()

            # Read the correct answer, split the line to get the correct answer letter, and convert to lowercase
            correct_answer = file_handle.readline().strip().split()[-1].lower()
            # .split() splits the string into a list where spaces are the delimiter
            # [-1] accesses the last element in the list, which is the answer letter
            # .lower() converts the string to lowercase

            # Print the question and answers
            print(question)
            print("a. " + answer1)
            print("b. " + answer2)
            print("c. " + answer3)
            print("d. " + answer4)

            # Get user's answer
            user_answer = input("Your answer (a, b, c, or d): ").strip().lower()
            # .strip() removes any leading or trailing whitespace, ensuring the user's input is clean
            # .lower() converts the input to lowercase to make the comparison case-insensitive
            print(f"you answered: {user_answer}")

            # Check if the answer is correct
            if user_answer == correct_answer:
                print("Correct!\n")
            else:
                print(f"Incorrect! The correct answer is {correct_answer}.\n")

# Call the main function directly
main()
