class Situation:
    
    def __init__(self, title, text, choices = []):
        self.title = title
        self.text = text
        self.choices = choices

    def makeChoice(self, choice, player):
        self.choices[choice].cons(player)