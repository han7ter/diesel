class Choice:
    def __init__(self, title, skills = False, conditions = False):
        self.title = title
        self.skills = skills
        self.conditions = conditions

    def cons(self, player):
        if self.conditions:
            if player.checkConditions(self.conditions):
                if self.skills: player.changeProp(self.skills)
            else:
                return False
        else:
            if self.skills: player.changeProp(self.skills)
        return player
        