class QuizBrain:

    def __init__(self, ques_list):
        self.ques_no = 0
        self.ques_list = ques_list

    def still_has_question(self):
        return self.ques_no < len(self.ques_list)

    def next_question(self):
        current_question = self.ques_list[self.ques_no]
        self.ques_no += 1
        user_answer = input(f"Q.{self.ques_no}: {current_question.text} (True/False):")
        return self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        return user_answer == correct_answer
