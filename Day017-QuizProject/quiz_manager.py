class QuizManager:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_no = 0
        self.score = 0

    def questions_left(self):
        return self.question_no < len(self.question_list)

    def display_question(self):
        current_q = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(
            f"Q.{self.question_no}: "
            f"{current_q.text} "
            "(True/False): "
        )
        self.check_answer(
            user_answer,
            current_q.answer
        )

    def check_answer(
            self,
            user_answer,
            correct_answer
    ):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(
            f"The correct answer was: "
            f"{correct_answer}"
        )
        print(
            f"Your current score is: "
            f"{self.score}/{self.question_no}"
        )

        print()