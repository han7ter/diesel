class Situation:
    
    def __init__(self, title, text, choices = [], textConditions = False):
        self.title = title
        self.text = text
        self.choices = choices
        self.textConditions = textConditions

    def makeChoice(self, choice, player):
        self.choices[choice].cons(player)

    def check(self, player):
        results = []
        for condition in self.textConditions:
            for variant in condition:
                if player.checkTextCondition(variant["condition"], variant["value"]):
                    results.append(variant["text"])
                    break
        self.text = self.text.format(*results)
        return True