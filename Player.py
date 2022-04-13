class Player:
    life = True
    health = 3

    def __init__(self, name, engene, sociable, body):
        self.name = name
        self.engene = engene
        self.sociable = sociable
        self.body = body

    def changeProp(self, skills):
        for prop, val in skills.items():
            if prop == "engene":
                self.engene += val
            elif prop == "sociable":
                self.sociable += val
            elif prop == "body":
                self.body += val

    def checkConditions(self, conditions):
        result = True
        for condition, value in conditions.items():
            if condition == "engene" and self.engene < value:
                result = False
                break
            elif condition == "sociable" and self.sociable < value:
                result = False
                break
            elif condition == "body" and self.body < value:
                result = False
                break
        return result

    def logSkills(self):
        print(f"Тело: {self.body}\nИнженерия: {self.engene}\nСоциальность: {self.sociable}")
