# TODO 1 - asking the question
# TODO 2 - check if answer is correct
# TODO 3 - check if we are at end of quiz

class QuizBrain:
    """Brain behind the whole quiz game"""

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    
    def still_has_questions(self):
        """Returns True if there are questions still remaining else returns False"""
        return self.question_number < len(self.question_list)
    
    
    def next_question(self):
        """Prints next question and gets user input"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    
    def check_answer(self, user_answer, correct_answer):
        """Checks if user answered correctly"""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
