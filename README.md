# BloonsTD6Bot

This "Bloons Tower Defense 6 Bot" was intended to be used to farm instant monkeys during time-limited 
events such as Easter or Halloween.

It is able to finish the map "Dark Castle" on easy difficulty, standard mode in less than 6 minutes. 
At the time of creation, this was the fastest way to farm instant monkeys.

## Prerequisite

- Own BTD6 on Steam
- Own a monitor of at least 1600x900 resolution
- Install Python3 (developed in Python 3.5.1)
- You might want to upgrade setuptools: `$ pip install setuptools -U`
- Install `pyautogui` through: `$ pip install pyautogui`

## Run

Starting the bot can be done using the following steps:

1. Run BTD6 from Steam, windowed, with a resolution of 1600x900 and leave it at the home menu
2. Run the bot: `$ python dark_castle.py`
3. During the starting of this bot, switch to the BTD6 game so it is the top most window ánd place your mouse on the top left corner of the BTD6 screen

The bot will now navigate the menu and start the game.

<sub>**Remark**: have the commandline and BTD6 open on the same monitor. 
This is a [known issue](https://github.com/asweigart/pyautogui/issues/9) of `pyautogui`.</sub>

## Stop

Stopping this bot, while it is clicking or searching the screen, is done in two ways:

- Move mouse to the top-left corner of the screen. This activates the failsafe of `pyautogui`. 
You can read more about this failsafe [here](https://pyautogui.readthedocs.io/en/latest/introduction.html#fail-safes).
- `Ctrl+C` in the commandline window

#

Enjoy!

\- JSP
