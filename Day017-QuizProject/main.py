from question import Question
from data import quiz_data
from quiz_manager import QuizManager

question_bank = []

for item in quiz_data:
    new_question = Question(
        item["question"],
        item["answer"]
    )
    question_bank.append(
        new_question
    )

quiz = QuizManager(
    question_bank
)

while quiz.questions_left():
    quiz.display_question()

print("You've completed the quiz")
print(
    f"Your final score was: "
    f"{quiz.score}/{quiz.question_no}"
)