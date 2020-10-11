### Deprecated

Before reading the instructions, please be aware that this project is not maintained anymore. I found that after each update of _Bloons TD 6_, all images of buttons, heroes and skills would be outdated. To still use the bot, please create your own snippets of those images and replace the ones in `./resources/`. If the flow of the menus was not changed, this should still work with the new images.

--------------

# BloonsTD6Bot

The BloonsTD6Bot is a farming bot for the popular tower defence game [_Bloons TD 6_](https://ninjakiwi.com/Games/Steam/Bloons-TD-6-Steam.html). 
It is intended to be used to farm [_Insta-Monkeys_](https://bloons.fandom.com/wiki/Insta-Monkey) during time-limited 
events such as Easter or Halloween. Bot navigation is done through fuzzy image matching.

The bot is able to finish the map _Dark Castle_ on easy difficulty, standard mode in less than 6 minutes. 
At the time of creation, this was the fastest way to farm _Insta-Monkeys_.

## Setup

#### Prerequisite

- _Bloons TD 6_ on [Steam](https://store.steampowered.com/app/960090/Bloons_TD_6/)
- Python3

#### Install

- (OPTIONAL) Create a Python virtual environment: `$ python -m venv btd6bot`
- (OPTIONAL) Activate the virtual environment
    - Windows: `$ btd6bot\Scripts\activate.bat` 
    - Unix & MacOS: `$ source btd6bot/bin/activate`
- You might need to upgrade setuptools: `$ pip install setuptools -U`
- Install requirements: `$ pip install -r requirements.txt`

## Start

Starting the bot can be done using the following steps:

1. Run _Bloons TD 6_  from Steam, windowed, with a resolution of 1600x900 and leave it at the home menu
2. Run the bot: `$ python dark_castle.py` for map _Dark Castle_
3. During the initialisation of this bot, switch to the _Bloons TD 6_ game so it is the top most window 
**and** place your mouse on the top left corner of this window

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
