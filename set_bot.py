"""Automatically clicks sets in the set game on setwithfriends.com. Takes about 10-14 seconds to find a set."""
import pyautogui, os

# CHANGE THESE CONSTANTS
SET_CARD_BOX_START = (675, 145) # Left top corner position of the set card box container
# Width and height normally 197 and 123 respectively on a monitor with a width greater than or equal to 1300 px
SET_CARD_WIDTH = 197 # Width of a set card 
SET_CARD_HEIGHT = 123 # Height of a set card

pyautogui.PAUSE = 0.07

def checkset(a, b, c):
    """Checks if 3 tuples with set card data are a set."""
    for i in range(4):
        if a[i] == b[i] == c[i]:
            pass
        elif a[i] != b[i] != c[i] and a[i] != c[i]:
            pass
        else:
            return False

    return True

set_cards = os.listdir("set_cards") # Set card images with this format: number-pattern-shape-color

def get_cards(set_cards):
    """Uses pyautogui.locateOnScreen to find all the set cards currently on the screen and set their values to their set data in a dictionary."""
    cur_cards = {}
    for card in set_cards:
        pos = pyautogui.locateCenterOnScreen("set_cards/" + card, region=(SET_CARD_BOX_START[0], SET_CARD_BOX_START[1], SET_CARD_WIDTH*3 + 30, SET_CARD_HEIGHT*5 + 30))
        if pos != None:
            cur_cards[tuple(card[:7].split("-"))] = pos
    return cur_cards

def click_set(cur_cards):
    """Cycles through every single set card combination and sees if they're a set. If so, click the set cards that make the set."""
    cards_list = list(cur_cards.keys())
    for card in cards_list:
        cards_without1 = cards_list[:]
        try:
            cards_without1.remove(card)
        except ValueError:
            pass
        for card2 in cards_without1:
            cards_without2 = cards_without1[:]
            try:
                cards_without2.remove(card)
            except ValueError:
                pass
            for card3 in cards_without2:
                if checkset(card, card2, card3):
                    pyautogui.moveTo(cur_cards.get(card))
                    pyautogui.click()
                    pyautogui.moveTo(cur_cards.get(card2))
                    pyautogui.click()
                    pyautogui.moveTo(cur_cards.get(card3))
                    pyautogui.click()
                    return 

pyautogui.click()
width, height = pyautogui.size()
while True:
    pyautogui.moveTo((width - 20, height - 20))
    cur_cards = get_cards(set_cards)
    if cur_cards != {}:
        click_set(cur_cards)
    else:
        break



