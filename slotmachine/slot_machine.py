import emoji
from random import choice
faces = [emoji.emojize(":red_apple:"),
         emoji.emojize(":pear:"),
         emoji.emojize(":tangerine:")]


class Column:

    def __init__(self):
        self.face = choice(faces)

    def change_face(self):
        self.face = choice(faces)


class Slot:

    def __init__(self):
        self.x = Column()
        self.y = Column()
        self.z = Column()

    def take_bet(self, bet):
        self.bet = bet
        return bet

    def show_slot(self):
        print(self.x.face, self.y.face, self.z.face)

    def pull_handle(self):
        self.x.change_face()
        self.y.change_face()
        self.z.change_face()

    def score_slot(self, bet):
        if self.x.face == self.y.face == self.z.face:
            return self.bet * 2
        elif self.x.face == self.y.face or self.y.face == self.z.face or self.x.face == self.z.face:
            return self.bet * 1.5
        else:
            return 0
