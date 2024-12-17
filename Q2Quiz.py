# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.

def main():
    score = 0  # Initialize score

    with open("questions.txt", 'r') as file_handle:
        while True:
            # Read the question
            question = file_handle.readline().strip()
            if not question:  # Check if the question is empty (end of file)
                break

            # Read the answer choices and remove any extra whitespace
            answer1 = file_handle.readline().strip()
            answer2 = file_handle.readline().strip()
            answer3 = file_handle.readline().strip()
            answer4 = file_handle.readline().strip()

            # Read the correct answer, split the line to get the correct answer letter, and convert to lowercase
            correct_answer = file_handle.readline().strip().split()[-1].lower()

            # Print the question and answers without repeating letters
            print(question)
            print("a. " + answer1[3:])
            print("b. " + answer2[3:])
            print("c. " + answer3[3:])
            print("d. " + answer4[3:])

            # Get user's answer
            user_answer = input("Your answer (a, b, c, or d): ").strip().lower()
            print(f"You answered: {user_answer}")

            # Check if the answer is correct
            if user_answer == correct_answer:
                print("Correct!\n")
                score += 1  # Increment score for correct answer
            else:
                print(f"Incorrect! The correct answer is {correct_answer}.\n")

    # Print the final score
    print(f"Your final score is: {score}")

# Call the main function directly
main()
