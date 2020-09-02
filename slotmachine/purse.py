class Purse:

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
        format_funds = format(self.funds, '.2f')
        print("you have", format_funds)