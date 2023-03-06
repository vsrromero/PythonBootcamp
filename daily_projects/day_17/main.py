from question_model import Question
from quiz_brain import QuizBrain
from art import logo
import os

os.system('cls')

print(logo)

from data import question_data

question_bank = []

for q in question_data:
    question = q['question']
    answer = q['correct_answer']
    new_question = Question(question, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

score = quiz.score
number_of_questions = quiz.question_number

print("You've completed the quiz")
print(f"Your final score is {score} of {number_of_questions}.")

