#### Purse ####
Manages the players funds with methods that add, remove and checks the balance of their purse.
- Initial credit (defaults to 10)
- Adds winnnings to credit.
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
- Empty house - all 3 columns conains different values.