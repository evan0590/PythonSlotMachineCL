### Slot Machine ###
A simple command line version of a slot machine in Python. The slot machine consists of three columns that display 
one of three fruits.
When the slot machine begins, the player is asked to place a bet from their initial credit (defaults to 10). 

The player can exit the game at any time by typing ‘N’.

To play this game on your local machine it is necessary to have Python 3 installed on your machine.\
With this prerequisite fulfilled, run the following commands from the root directory of this project:
```json
python -m venv env
source env/bin/activate
pip install git+https://github.com/evan0590/PythonSlotMachineCL.git
run_slotmachine
```

This project contains the following three classes and their respective operations:

#### Purse ####
Manages the players funds with methods that add, remove and checks the balance of their purse.
- Initial credit (defaults to 10)
- Adds winnings to credit.
- Removes funds from credit and manages for bets larger than available funds.
- Displays available funds with two digits after the decimal point, using string formatting.

#### Column ####
Creates a face representing the fruit.
- Emoji fruits used.
- Changes the face at random.

#### Slot ####
Each slot has three columns representing the three fruits.
For each play of the slot machine there are three possible outcomes.
show_slot method prints the three random faces when called from the function below.
- Full house - all 3 columns contain the same value. -> Player wins an amount equal to the bet.
- Half house - 2 of the 3 columns contain the same value. -> Player wins half the amount bet.
- Empty house - all 3 columns contain different values.