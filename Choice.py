class Choice:
    def __init__(self, title, prop, difference):
        self.title = title
        self.prop = prop
        self.difference = difference

    def cons(self, player):
        # Вместо этого вызови метод player.changeProp(self.prop, self.difference)
        player[self.prop] += self.difference
        return player
        