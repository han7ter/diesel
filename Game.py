import tkinter
from tracemalloc import start
class Game(tkinter.Tk):

    status = "menu"

    def _init__(self):
        super().__init__()
        self.geometry("700x700")
        self.title("Diesel")

    def start(self, story):
        self.story = story
        self.status = "game"
        self.showStory()

    def showMenu(self):
        self.head = tkinter.Label(self, text = "МЕНЮ")
        self.button1 = tkinter.Button(self, text = "новая игра", command = start)
        self.button2 = tkinter.Button(self, text = "загрузить игру")
        self.button3 = tkinter.Button(self, text = "выйти из игры")
        self.head.pack()
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

    def clearWindow(self):
        print("Метод очистки экрана")
    
    def showStory(self):
        self.storyTitle = tkinter.Label(self, text = self.story.getCurrentSituation().title)
        self.storyText  = tkinter.Label(self, text = self.story.getCurrentSituation().text)
        self.storyTitle.pack()
        self.storyText.pack()
