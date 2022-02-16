import tkinter
class Game(tkinter.Tk):

    status = "menu"

    def _init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("Diesel")

    def start(self, story):
        self.story = story
        self.status = "game"
        self.showStory()
    
    def showStory(self):
        self.storyTitle = tkinter.Label(self, text = self.story.getCurrentSituation().title)
        self.storyText  = tkinter.Label(self, text = self.story.getCurrentSituation().text)
        self.storyTitle.pack()
        self.storyText.pack()
