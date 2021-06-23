# Set Bot

Automatically clicks sets in the set game on [setwithfriends.com](). Does this by using the pyautogui module to locate set cards, then going through every set card combination to find a set, and using pyautogui to click the set cards. Locating set cards takes around 10-14 seconds on my machine.

View set rules at: [https://setwithfriends.com/help]()

Set card data in form (_number_, _pattern_, _shape_, _color_)

`set_bot.py` has constants to change that depend on your screen size 

**Please don't use this program in public games without permission from the person who started the game. This program's intent is not to make people not have fun while playing on setwithfriends** 

#### How to run:
1. Make sure you are in the directory with the code
2. Open [setwithfriends.com]()
3. Join a game or create your own and wait for it to start or start it
4. With your mouse hovering over something unimportant, on the setwithfriends.com website, run `python set_bot.py`
5. To stop the program, go to the terminal window and press ctrl+c.

