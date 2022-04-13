from Situation import Situation
from Choice import Choice
class Story:

    chapters = {
        "Детство" : [
            Situation("2 года, лето", "Вас впервые оставили одного в комнате. Окно было открыто, и с улицы был слышен гул проезжающих мимо дома машин и громкие голоса людей. В противоположном от окна углу был короб с вашими игрушками.", [Choice("Подойти к окну", {"sociable" : 1, "body" : 1}), Choice("Подойти к игрушкам", {"engene" : 1, "body" : 1})]),
            Situation("3 года, весна", "Сегодня ты впервые посетил городской сад. За 3 года жизни ты привык к грязным и шумным улицам. Вид сада тебя завораживал ты впервые видел так много деревьев в одном месте. После прихода к власти фабрикантов на улицах вырубили все деревья, а те, которые остались, погибли от загрязненного воздуха.", [Choice("сесть", {"body" : -1}), Choice("Побежать", {"body" : 1})]),
            Situation("4 года, лето", "Вы сидели в комнате и играли в игрушки, окно было открыто. Вдруг к вам в комнату залетела птица. У неё был необычный окрас, синие крылья и красное пузо. Она начала громко кричать: \"Все будет хорошо, все будет хорошо\". Вы сильно напугались и побежали к маме. Она вас успокоила и объяснила, что это был соседский попугай, который скорее всего сбежал из клетки. Через некоторое время вы вернулись к себе в комнату, птица всё ещё сидела в ней. Вам это не нравится- \"надо как-то убрать попугая отсюда \", говорите вы вслух.", [Choice("Поймать попугая голыми руками и выкинуть в окно", {"body" : 1}), Choice("Уговорить попугая улететь", {"sociable" : 1})]),
            Situation("5 лет, зима","Вы сидите в своей комнате и играете в конструктор. Из коридора начало доноситься множество голосов. Вас это заинтересовало, и вы вышли посмотреть что происходит. Оказалось к вам приехали ваши родственники из соседнего города. Их первыми словами обращенными к вам были: \"Как же ты подрос! Каким большим стал.\". Вы видели их в первый раз, но сделали вид, что помните их. Они подарили вам интересный конструктор. Взрослые пошли в гостинную комнату и оставили вас одного в коридоре. Вы думаете куда вам пойти...", [Choice("Пойти в гостинную комнату к гостям и поговорить с ними", {"sociable" : 1}), Choice("Пойти играть к себе в комнату в конструктор", {"engene" : 1})]),
            Situation("6 лет, лето", "Вечером вы сидите с семьёй за столом. Вы как обычно не хотите есть фасоль на ужин. Тут ваш отец обращается к вам: \"Сын, ты ведь знаешь, что в сентябре ты уже идешь в первый класс?\". Вы ответили, что конечно же не забыли об этом, хотя это было так. \"Ты уже определился со своим профилем?\",- сказал отец. \"Напомни пожалуйста, какие профили есть\"- спрашиваете вы у отца. Папа говорит вам: \"Есть три профиля, первый - математический, на нём ты будешь изучать точные науки и сможешь в будующем стать учёным или инженером. Второй - социальный, ты будешь изучать инструменты по взаимодействию с обществом и сможешь стать агитатором и помогать гос-ву поддерживать порядок в империи. И третий - военный, ты будешь обучаться в кадетском училище и станешь храбрым защитником нашей империи\". Вы говорите... ", [Choice("Математичсекий", False, {"engene" : 3}), Choice("Социальный", False, {"sociable" : 3}), Choice("Военный", False, {"body" : 3})])
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

    