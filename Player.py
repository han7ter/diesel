class Player:                          #др героя - 2400 октябрь
    life = True
    health = 3
    className = False

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
            elif prop == "className":
                self.className = val
            elif prop == "book":
                self.book = val

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

    def checkTextCondition(self, condition, value):
        if condition == "engene" and self.engene != value:
            return False
        elif condition == "sociable" and self.sociable != value:
            return False
        elif condition == "body" and self.body != value:
            return False
        elif condition == "className" and self.className != value:
            return False
        elif condition == "book" and self.book != value:
            return False
        return True

    def logSkills(self):
        print(f"Тело: {self.body}\nИнженерия: {self.engene}\nСоциальность: {self.sociable}")
