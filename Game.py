import tkinter
from tkinter import messagebox

from Player import Player

from Story import Story
class Game(tkinter.Tk):

    status = "menu"
    points = 5

    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("Diesel")

    def start(self, player):
        self.story = Story()
        self.player = Player(**player)
        self.status = "game"
        self.clearWindow()
        self.showStory()

    def getPlayerName(self):
        self.clearWindow()
        self.nameTitle = tkinter.Label(self, text = "Введите имя", font="Verdana 20")
        self.nameTitle.pack()
        self.name = tkinter.Entry(self)
        self.name.pack()
        self.button = tkinter.Button(self, text = "далее", command=self.createPlayer)
        self.button.pack()

    def createPlayer(self):
        name = self.name.get()

        skills = {
            "engene" : 0,
            "sociable" : 0,
            "body" : 0
        }

        def increase(prop):
            if self.points > 0 and skills[prop] < 5:
                self.points -= 1
                skills[prop] += 1
                updateScores()
            if self.points == 0:
                skills["name"] = name
                self.nextButton = tkinter.Button(self, text = "далее", command = lambda player = skills:self.start(player))
                self.nextButton.grid(column = 3, row = 5)

        def decrease(prop):
            if self.points < 5 and 0 < skills[prop]:
                self.points += 1
                skills[prop] -= 1
                updateScores()

        
        def updateScores():
            self.pointsText.configure(text=self.points)
            print(self.skillElements)
            for skill, val in skills.items():
                self.skillElements[skill].configure(text=val)


        self.clearWindow()
        self.nameTitle = tkinter.Label(self, text = name, font="Verdana 20")
        self.nameTitle.grid(column=1, row=0)
        self.pointsText = tkinter.Label(self, text = self.points, font="Verdana 20")
        self.pointsText.grid(column = 2, row = 0)

        self.skillElements = {}
        i = 0
        for skill, val in skills.items():
            self.skillName = tkinter.Label(self, text = skill)
            self.skillName.grid(column=0, row=1 + i)

            self.skillMinus = tkinter.Button(self, text = "-", command = lambda skill = skill: decrease(skill))
            self.skillMinus.grid(column=1, row=1 + i)

            self.skillPlus = tkinter.Button(self, text = "+", command = lambda skill = skill: increase(skill))
            self.skillPlus.grid(column=3, row=1 + i)

            self.skillElements[skill] = tkinter.Label(self, text = val)
            self.skillElements[skill].grid(column=2, row= 1 + i)

            i += 1


    def showMenu(self):
        self.head = tkinter.Label(self, text = "МЕНЮ")
        self.button1 = tkinter.Button(self, text = "новая игра", command = self.getPlayerName)
        self.button2 = tkinter.Button(self, text = "загрузить игру")
        self.button3 = tkinter.Button(self, text = "выйти из игры")
        self.head.pack()
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

    def clearWindow(self):
        for widget in self.winfo_children():
            widget.destroy()

    def nextStory(self):
        self.story.nextSituation()
        self.clearWindow()
        self.showStory()

    def showStory(self):
        situation = self.story.getCurrentSituation()
        self.storyTitle = tkinter.Label(self, text = situation.title, font="Verdana 20")
        if situation.textConditions:
            situation.check(self.player)
        self.storyText  = tkinter.Label(self, text = self.wrap(situation.text,77))
        self.storyTitle.pack()
        self.storyText.pack()
        self.choiceButtons = []
        def makeChoice(choice):
            p = choice.cons(self.player)
            if p:
                self.player = p
                self.nextStory()
                self.player.logSkills()
            else:
                messagebox.showerror("Ошибка","Не хватает очков для выбора")
                
        if len(situation.choices) > 0:
            for choice in situation.choices:
                choiceButton = tkinter.Button(self, text = choice.title, command = lambda choice = choice: makeChoice(choice))
                self.choiceButtons.append(choiceButton)
                choiceButton.pack()
        else:
            choiceButton = tkinter.Button(self, text = "Далее", command = self.nextStory)
            self.choiceButtons.append(choiceButton)
            choiceButton.pack()




    def wrap(self, text, length):
        words = text.split()
        lines = []
        line = ''
        for w in words:
            if len(w) + len(line) > length:
                lines.append(line)
                line = ''
            line = line + w + ' '
            if w is words[-1]: lines.append(line)
        return '\n'.join(lines)
    
