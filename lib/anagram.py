# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, new_word):
        return [word for word in new_word if sorted(self.word) == sorted(word.lower())]
