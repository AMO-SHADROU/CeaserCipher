class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        if self.question_number >= len(self.question_list):
            return False
        return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        print(f"Q.{self.question_number}: {current_question.text}")
        user_answer = input("True or False?:  ")
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print(f"The answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print()
