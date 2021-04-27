# For now, I'= won't be working on this exercise. Asking for FRP is a bit too much for me right now ^^

# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING


    def guess(self, char):
        self.remaining_guesses -= 1


    def get_masked_word(self):
        pass

    def get_status(self):
        pass
