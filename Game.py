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

    def showMenu(self, story):
        self.head = tkinter.Label(self, text = "МЕНЮ")
        self.button1 = tkinter.Button(self, text = "новая игра", command = lambda story = story: self.start(story))
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
        self.storyTitle = tkinter.Label(self, text = self.story.getCurrentSituation().title, font="Verdana 20")
        self.storyText  = tkinter.Label(self, text = self.wrap(self.story.getCurrentSituation().text,77))
        self.button4 = tkinter.Button(self, text = "далее", command = self.nextStory)
        self.storyTitle.pack()
        self.storyText.pack()
        self.button4.pack()

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
    
