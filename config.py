import logging
import sys


def init_logging():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.DEBUG,
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )


# Bot

PYAUTOGUI_SLEEP_SECONDS_BETWEEN_CALLS = 1
START_SLEEP_SECONDS = 10

DO_OPEN_MONKEYS = False

CLICK_ON_MATCHING_CONFIDENCE = 0.9
WAIT_FOR_MATCHING_CONFIDENCE = 0.9525

RELOAD_TOWER_COUNTER = 3

CHECK_LEVEL_UP_COUNTER = 30
CHECK_GAME_PAUSED_COUNTER = 30
CHECK_DEFEATED_COUNTER = 20

LOGS_DIR = '_logs'

# Menu
BUTTON_MENU_PLAY = 'resources/menu/button_menu_play.jpg'
BUTTON_MENU_MAPS_EXPERT = 'resources/menu/button_menu_maps_expert.jpg'
BUTTON_MENU_EASY_DIFF = 'resources/menu/button_menu_easy_diff.jpg'
BUTTON_MENU_STANDARD_MODE = 'resources/menu/button_menu_standard_mode.jpg'

BUTTON_GAME_START = 'resources/menu/button_game_start.jpg'
BUTTON_GAME_FAST_FORWARD = 'resources/menu/button_game_fast_forward.jpg'
BUTTON_GAME_TO_HOME = 'resources/menu/button_game_to_home.jpg'
BUTTON_GAME_RESTART = 'resources/menu/button_game_restart.jpg'
BUTTON_GAME_RESTART_CONFIRM = 'resources/menu/button_game_confirm_restart.jpg'
BUTTON_GAME_FREEPLAY = 'resources/menu/button_game_freeplay.jpg'

PROMPT_DEFEAT = 'resources/menu/prompt_defeat.jpg'
PROMPT_LEVEL_UP = 'resources/menu/prompt_level_up.jpg'

PROMPT_OVERWRITE = 'resources/menu/prompt_overwrite.jpg'
BUTTON_OVERWRITE_OK = 'resources/menu/button_overwrite_ok.jpg'

# Events
COLLECTION_XS = range(50, 1500, 50)
COLLECTION_Y = 450

BUTTON_EVENT_COLLECT = 'resources/menu/button_event_collect.jpg'
BUTTON_EVENT_CONTINUE = 'resources/menu/button_event_continue.jpg'

# Towers
TOWER_NINJA_UPGRADE = 'resources/towers/ninja/upgrade_{}_{}.jpg'
TOWER_SUPER_UPGRADE = 'resources/towers/super/upgrade_{}_{}.jpg'

# Heroes
HERO_SELECTED_OBYN_1 = 'resources/towers/heroes/obyn_1.jpg'
HERO_SELECTED_OBYN_2 = 'resources/towers/heroes/obyn_2.jpg'

HERO_SELECTED = {'obyn': [HERO_SELECTED_OBYN_1, HERO_SELECTED_OBYN_2]}

# Maps

# Dark Castle
MAPS_DARK_CASTLE = 'resources/maps/dark_castle/map.jpg'

MAPS_POS_DARK_CASTLE_INTERSECTION_TOP = 'resources/maps/dark_castle/intersection_top_path.jpg'
MAPS_POS_DARK_CASTLE_INTERSECTION_BOTTOM = 'resources/maps/dark_castle/intersection_bottom_path.jpg'
MAPS_POS_DARK_CASTLE_TOP_LEFT_MAIN_ROAD = 'resources/maps/dark_castle/top_left_main_road.jpg'

MAPS_ROUND_DARK_CASTLE_4 = 'resources/maps/dark_castle/round_4.jpg'  # 23
MAPS_ROUND_DARK_CASTLE_20 = 'resources/maps/dark_castle/round_20.jpg'  # 163

# Hotkeys
HOTKEY_UPGRADE_1 = ','
HOTKEY_UPGRADE_2 = ';'
HOTKEY_UPGRADE_3 = ':'
HOTKEY_UPGRADES = [HOTKEY_UPGRADE_1, HOTKEY_UPGRADE_2, HOTKEY_UPGRADE_3]

HOTKEY_HERO = 'u'
HOTKEY_TOWER_NINJA = 'd'
HOTKEY_TOWER_SUPER_MONKEY = 's'
