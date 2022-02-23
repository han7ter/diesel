from Situation import Situation
class Story:

    chapters = {
        "Детство" : [
            Situation("2 года", "Вам 2 года."),
            Situation("3 года", "Прогулка в саду с мамой"),
            Situation("4 года", "ваша болезнь"),
            Situation("5 лет","подготовка к школе")
        ]
    }
    currentChapter = "Детство"
    currentSituation = 0

    def nextSituation(self):
        if self.currentSituation >= len(self.chapters[self.currentChapter]) - 1:
            return False
        else:
            self.currentSituation += 1
        return True


    def getCurrentSituation(self):
        return self.chapters[self.currentChapter][self.currentSituation]