import random

class flashcard:
    def __init__(self): 
        self.fruits={'apple':'red',
                     'orange':'orange',
                     'banana':'yellow'}
    def quiz(self):
        while(True):
            fruit,color = random.choice(list(self.fruits.items()))
            print("what is the color of {}".format(fruit))
            user_answer = input()
            if (user_answer.lower()==color):
                print("correct answer")
            else:
                print("wrong answer")
            option = int(input("enter 0, if you want to,play again guys:"))
            if (option):
                break
print("Welcome to fruit quiz")
fc=flashcard()
fc.quiz()