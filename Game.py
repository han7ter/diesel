import tkinter
class Game(tkinter.Tk):

    status = "menu"

    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("Diesel")

    def start(self, story):
        self.story = story
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
        points = 5

        skills = {
            "engene" : 0
        }

        def increase(prop):
            global points
            points -= 1
            skills[prop] += 1

        def decrease(prop):
            global points
            points += 1
            skills[prop] -= 1

        self.clearWindow()
        self.nameTitle = tkinter.Label(self, text = name, font="Verdana 20")
        self.nameTitle.grid(column=1, row=0)
        self.points = tkinter.Label(self, text = points, font="Verdana 20")
        self.points.grid(column = 2, row = 0)
        self.engene = tkinter.Label(self, text = "Инженерия")
        self.engene.grid(column=0, row=1)
        self.buttonMinusEngene = tkinter.Button(self, text = "-", command = decrease("engene"))
        self.buttonMinusEngene.grid(column=1, row=1)

        self.buttonPlusEngene = tkinter.Button(self, text = "+", command = increase("engene"))
        self.buttonPlusEngene.grid(column=3, row=1)

        self.SchetEngene = tkinter.Label(self, text = skills["engene"])
        self.SchetEngene.grid(column=2, row= 1)


    def showMenu(self, story):
        self.head = tkinter.Label(self, text = "МЕНЮ")
        # self.button1 = tkinter.Button(self, text = "новая игра", command = lambda story = story: self.start(story))
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
        self.storyText  = tkinter.Label(self, text = self.wrap(situation.text,77))
        self.storyTitle.pack()
        self.storyText.pack()
        self.choiceButtons = []
        for choice in situation.choices:
            choiceButton = tkinter.Button(self, text = choice.title)#, command = lambda player = player: self.cons(player))
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
    
