from Situation import Situation
from Choice import Choice
class Story:

    chapters = {
        "Детство" : [
            Situation("2 года", "Вас впервые оставили одного в комнате. Окно было открыто, и с улицы был слышен гул проезжающих мимо дома машин и громкие голоса людей. В противоположном от окна углу был короб с вашими игрушками.", [Choice("Подойти к окну", "sociable", 1), Choice("Подойти к игрушкам", "engene", 1)]),
            Situation("3 года", "Сегодня ты впервые посетил городской сад. За 3 года жизни ты привык к грязным и шумным улицам. Вид сада тебя завораживал ты впервые видел так много деревьев в одном месте. После прихода к власти фабрикантов на улицах вырубили все деревья, а те, которые остались, погибли от загрязненного воздуха."),
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