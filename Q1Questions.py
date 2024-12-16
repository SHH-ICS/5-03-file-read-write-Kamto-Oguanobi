# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.

# opens file
file_handle = open("questions.txt", 'w')

#  asks for question
question = input("Enter the question  ")
#  ye
answer1 = input("first answer : ")
answer2 = input("second answer choice: ")
answer3 = input("third answer choice: ")
answer4 = input("fourth answer choice: ")
correct_answer = input("Letter of the answer (a b c d): ")

# Write the question and answers to the file
file_handle.write(question + "\n")
file_handle.write("a. " + answer1 + "\n")
file_handle.write("b. " + answer2 + "\n")
file_handle.write("c. " + answer3 + "\n")
file_handle.write("d. " + answer4 + "\n")
file_handle.write("Correct answer: " + correct_answer + "\n")
