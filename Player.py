class Player:
    life = True
    health = 3

    def __init__(self, name, engene, sociable, body):
        self.name = name
        self.engene = engene
        self.sociable = sociable
        self.body = body

    def changeProp(self, prop, val):
        # Допиши остальные условия для разных скиллов
        if prop == "engene":
            self.engene += val
