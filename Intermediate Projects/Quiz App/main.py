from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [] 

for question in question_data:
    ques = Question(question["text"], question["answer"])
    question_bank.append(ques)

quiz = QuizBrain(question_bank)
score = 0

while quiz.still_has_question():
    if quiz.next_question():
        score += 1
        print("Correct Answer!")
        print(f"Your Score: {score}/{quiz.ques_no}")
    else:
        print("Wrong Answer!")

print("\n=====================================")
print("Quiz Completed!")
print(f"Total Question: {len(quiz.ques_list)}")
print(f"Total Score: {score}")
