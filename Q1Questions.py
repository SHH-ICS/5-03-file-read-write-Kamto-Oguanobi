# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.

# Still dont understand how this works
file_handle = open("questions.txt", 'w')

#  
question = input("Enter the question  ")
# 
answer1 = input("Enter the first answer choice: ")
answer2 = input("Enter the second answer choice: ")
answer3 = input("Enter the third answer choice: ")
answer4 = input("Enter the fourth answer choice: ")
correct_answer = input("Enter the letter of the correct answer (a b c d): ")

# Write the question and answers to the file
file_handle.write(question + "\n")
file_handle.write("a. " + answer1 + "\n")
file_handle.write("b. " + answer2 + "\n")
file_handle.write("c. " + answer3 + "\n")
file_handle.write("d. " + answer4 + "\n")
file_handle.write("Correct answer: " + correct_answer + "\n")

# Close the file
file_handle.close()

print("Question and answers have been saved to questions.txt.")
