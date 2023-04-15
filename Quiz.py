import random

NUMBER_OF_QUESTIONS = 5


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, quiz_name, grade):
        self.grades.append([quiz_name, grade])

    def show_grades(self):
        print(self.name)
        for grade in self.grades:
            print(f"{grade[0]} ---> {grade[1]}")


class Quiz:
    def __init__(self, name):
        self.name = name
        self.questions = [["5+5", "10"], ["12-3", "9"], ["22*4", "88"], ["14/2", "7"], ["0+0", "0"], ["33/11", "3"]]

    def list_questions(self):
        for index, question in enumerate(self.questions):
            print(f"{index + 1}. {question[0]}")

    def add_question(self):
        question = input("Type question: ")
        answer = input("Answer to question: ")
        self.questions.append([question, answer])

    def remove_question(self):
        self.list_questions()
        remove_index = int(input("Which question to remove? (Index)"))
        self.questions.pop(remove_index - 1)

    def initiate_quiz(self):
        correct_answers = 0
        if len(self.questions) >= NUMBER_OF_QUESTIONS:
            for index, question in enumerate(random.sample(self.questions, NUMBER_OF_QUESTIONS)):
                print(f"{index + 1}. {question[0]}")
                if input("Answer: ") == question[1]:
                    correct_answers += 1
            return self.grade_quiz(correct_answers)
        else:
            return "Not enough questions"

    def grade_quiz(self, points):
        grades = ["F", "E", "D", "C", "B", "A"]
        return grades[points]


def run():
    michal = Student("Michal Krsik")
    mat1 = Quiz("Matematika 1")

    michal.add_grade("Matematika 1", mat1.initiate_quiz())
    michal.show_grades()

