import emoji
from random import choice
faces = [emoji.emojize(":red_apple:"),
         emoji.emojize(":pear:"),
         emoji.emojize(":tangerine:")]

class Purse():

    def __init__(self):
        self.funds = 10

    def credit(self, bet):
        self.funds = self.funds + bet

    def debit(self, bet):
        if self.funds < bet:
            pass
        else:
            self.funds = self.funds - bet

    def get_balance(self):
        formatfunds = format(self.funds, '.2f')
        print("you have", formatfunds)

class Column():

    def __init__(self):
        self.face = choice(faces)

    def change_face(self):
        self.face = choice(faces)


class Slot():

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


def main():
    """Slot machine function that runs the code
    contained within the three classes above.

    Will only accept integers, will not account
    for floating point values placed as bets.
    """

    # Create wallet object from Purse class.
    wallet = Purse()
    # Create slot machine object from Slot class.
    machine = Slot()
    print("==========  SLOT MACHINE  ==========")
    print("Minimum bet is 2. Type 'N' to exit. ")
    wallet.get_balance()
    while wallet.funds > 1:
        # The player is asked to place a bet.
        bet = input("How much do you bet: ")
        # The player has the option to quit the game by typing 'N'.
        if bet == "N":
            print("You typed 'N' - Thank you for playing.")
            break
        elif bet == "n":
            print("You typed 'N' - Thank you for playing.")
            break
        else:
            try:
                # Convert bet to an integer value.
                gamble = machine.take_bet(int(bet))
            # Exception handling for when
            # non-integer value is entered.
            except ValueError:
                pass
            else:
                # Minimum bet is 2.
                if gamble < 2:
                    pass
                # Checking if integer is within available credit.
                elif gamble > wallet.funds:
                    wallet.debit(gamble)
                # A valid number within credit has been entered.
                else:
                    wallet.debit(gamble)
                    machine.pull_handle()
                    machine.show_slot()
                    wallet.credit(machine.score_slot(bet))
                    # Display, using string formatting,
                    # available funds with two
                    # digits after the decimal place.
                    fundsformat = format(wallet.funds, '.2f')
                    # Player cannot continue if funds are below 2.
                    if wallet.funds < 2:
                        print("You score", machine.score_slot(bet), "- Thank you for playing.")
                        print("You are leaving with ", fundsformat, ".", sep='')
                    # Player loses bet.
                    elif machine.score_slot(bet) == 0:
                        print("You score", machine.score_slot(bet), "- you have", fundsformat)
                    else:
                        print("You score", machine.score_slot(bet), "- you have", fundsformat)

if __name__ == '__main__':
    main()