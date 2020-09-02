from slotmachine.purse import Purse
from slotmachine.slot_machine import Slot


def main():
    """Slot machine function that runs the code
    contained within the classes imported above.

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
                    funds_format = format(wallet.funds, '.2f')
                    # Player cannot continue if funds are below 2.
                    if wallet.funds < 2:
                        print("You score", machine.score_slot(bet), "- Thank you for playing.")
                        print("You are leaving with ", funds_format, ".", sep='')
                    # Player loses bet.
                    elif machine.score_slot(bet) == 0:
                        print("You score", machine.score_slot(bet), "- you have", funds_format)
                    else:
                        print("You score", machine.score_slot(bet), "- you have", funds_format)


if __name__ == '__main__':
    main()
