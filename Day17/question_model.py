# Name of the class always PascalCase

class Question:
    """Models the question that will be used in quiz"""
    
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer