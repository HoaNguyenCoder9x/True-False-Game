from data import question_data
import random


class PlayGame:
    def __init__(self):
        self.question_num = 1
        self.current_score = 0
        self.live = 5
        self.playtime = True

    def getRandom(self):
        """ Get random question_answer from data"""
        get_random_question = random.choice(question_data)
        return get_random_question

    def checkGuess(self):
        guess = input().lower()
        if guess == answer:
            print("You got it right!")
            self.current_score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {answer}.")
        print(f"Your current score is: {self.current_score}/{self.question_num}")
        self.question_num += 1


play = PlayGame()
while play.playtime:
    question = play.getRandom()['text']
    answer = play.getRandom()['answer'].lower()
    print(f"Q.{play.question_num}: {question}. (True/False)")
    play.checkGuess()
