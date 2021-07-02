# Set Bot

Automatically clicks sets in the set game on [setwithfriends.com](https://setwithfriends.com). Does this by using the pyautogui module to locate set cards, then going through every set card combination to find a set, and using pyautogui to click the set cards. Locating set cards takes around 10-14 seconds on my machine.

View set rules at: https://setwithfriends.com/help/.

Set card data in form (_number_, _pattern_, _shape_, _color_).

`set_bot.py` has constants to change that depend on your screen size. To get `SET_CARD_BOX_START`, place your mouse at the top left corner of the box containing the set cards on [setwithfriends.com](https://setwithfriends.com) and run `python -c "import pyautogui; pos = pyautogui.position(); print((pos.x, pos.y))"`, which imports pyautogui and uses it's `position` function to get your mouse position. To get `SET_CARD_WIDTH` and `SET_CARD_HEIGHT`, move your mouse to the top left corner of any set card and make sure no grey border appears around the set card (if there is a border, move your mouse more up left). Then, press right click and click Inspect Element in the right click menu. If the screen resizes, make the HTML inspector smaller until the set cards are the same size as before. In the HTML inspector, a div element should be highlighted. Hover over it, and dimensions of the set card should appear above the set card. `SET_CARD_WIDTH` is the value left of the x, and `SET_CARD_HEIGHT` is the value to the right of the x.

**Please don't use this program in public games without permission from the person who started the game. This program's intent is not to make people not have fun while playing on setwithfriends.** 

## How to run:
1. Make sure you are in the directory with the code
2. Open [setwithfriends.com](https://setwithfriends.com)
3. Join a game or create your own and wait for it to start or start it
4. With your mouse hovering over something unimportant, on the setwithfriends.com website, run `python set_bot.py`
5. To stop the program, go to the terminal window and press ctrl+c

