# TODO 1 - asking the question
# TODO 2 - check if answer is correct
# TODO 3 - check if we are at end of quiz

class QuizBrain:
    """Brain behind the whole quiz game"""

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    
    def still_has_questions(self):
        """Returns True if there are questions still remaining else returns False"""
        return self.question_number < len(self.question_list)
    
    
    def next_question(self):
        """Prints next question and gets user input"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")