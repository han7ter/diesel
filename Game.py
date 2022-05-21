import tkinter
import json
from tkinter import messagebox

import os

from Player import Player

from Story import Story
class Game(tkinter.Tk):

    status = "menu"
    points = 5

    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("Diesel")

    def start(self, player, chapter = "Детство", situation = 0):
        self.story = Story(chapter, situation)
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
        self.button2 = tkinter.Button(self, text = "загрузить игру", command = self.loadGame)
        self.button3 = tkinter.Button(self, text = "выйти из игры", command = self.destroy)
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
            self.ButtonSave = tkinter.Button(self, text = "Сохранить", command = self.popup_win)
            self.ButtonSave.pack()
        else:
            choiceButton = tkinter.Button(self, text = "Далее", command = self.nextStory)
            self.choiceButtons.append(choiceButton)
            choiceButton.pack()
            self.ButtonSave = tkinter.Button(self, text = "Сохранить", command = self.popup_win)
            self.ButtonSave.pack()


    def save(self,tp):
        for widget in tp.winfo_children():
            if isinstance(widget, tkinter.Entry):
                print(widget.get())
                savedict = {
                    "name" : self.player.name,
                    "situation" : self.story.currentSituation,
                    "chapter" : self.story.currentChapter,
                    "engene" : self.player.engene,
                    "sociable" : self.player.sociable,
                    "body" : self.player.body,
                    "className" : self.player.className,
                    "book" : self.player.book
                }
                y = json.dumps(savedict)
                f = open(f"C:\python\projects\diesel\saves\{widget.get()}.json", "w")
                f.write(y)
                f.close()
        tp.destroy()
        

    def popup_win(self):
        tp = tkinter.Toplevel(self)
        tp.geometry("500x200")

        entry1= tkinter.Entry(tp, width= 20)
        entry1.pack()

        button1= tkinter.Button(tp, text="ok", command=lambda:self.save(tp))
        button1.pack(pady=5, side= tkinter.TOP)


    def loadGame(self):
        savewind = tkinter.Toplevel(self)
        savewind.geometry("500x200")
        names = os.listdir("C:\python\projects\diesel\saves")
        for files in names:
            a = files
            for i in range(5):
                files = files[:-1]
            button = tkinter.Button(savewind, text = f"{files}", command = lambda savewind = savewind, a = a:self.loadSave(savewind, a))
            button.pack()

    def loadSave(self, savewind, a):
        f = open(f"C:\python\projects\diesel\saves\{a}", "r")
        save = json.loads(f.read())
        print(save)

        savewind.destroy()

        skills = {
            "name" : save["name"],
            "engene" : save["engene"],
            "sociable" : save["sociable"],
            "body" : save["body"],
            "className" : save["className"],
            "book" : save["book"]
        }
        self.start(skills, save["chapter"], save["situation"])
        


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
    
