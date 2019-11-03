import logging
import sys


def init_logging():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )


# Bot

PYAUTOGUI_SLEEP_SECONDS_BETWEEN_CALLS = 1
START_SLEEP_SECONDS = 5
RELOAD_TOWER_COUNTER = 3
LEVEL_UP_COUNTER = 30
GAME_PAUSED_COUNTER = 30
FAIL_CHECK_COUNTER = 20

LOGS_DIR = '_logs'

# Menu
BUTTON_PLAY = 'resources/menu/button_play.png'
BUTTON_START_LEVEL = 'resources/menu/button_start_level.png'
BUTTON_FAST_FORWARD = 'resources/menu/button_fast_forward.png'

BUTTON_LEVEL_TO_HOME = 'resources/menu/button_level_to_home.png'
PROMPT_DEFEAT = 'resources/menu/prompt_defeat.png'
PROMPT_LEVEL_UP = 'resources/menu/prompt_level_up.png'

BUTTON_EVENT_COLLECT = 'resources/menu/button_event_collect.png'
BUTTON_EVENT_CONTINUE = 'resources/menu/button_event_continue.png'
BUTTON_EVENT_COLLECT_BLUE = 'resources/menu/button_event_collect_blue.png'
BUTTON_EVENT_COLLECT_PURPLE = 'resources/menu/button_event_collect_purple.png'
BUTTON_EVENT_COLLECT_MONKEYS = [BUTTON_EVENT_COLLECT_BLUE, BUTTON_EVENT_COLLECT_PURPLE]

BUTTON_EXPERT_MAPS = 'resources/menu/button_maps_expert.png'
BUTTON_EASY_DIFF = 'resources/menu/button_easy_diff.png'
BUTTON_STANDARD_MODE = 'resources/menu/button_standard_mode.png'

BUTTON_UPGRADES = 'resources/menu/button_upgrades.png'

PROMPT_OVERWRITE = 'resources/menu/prompt_overwrite.png'
BUTTON_OVERWRITE_OK = 'resources/menu/button_overwrite_ok.png'

# Towers
HERO_OBYN = 'resources/towers/heroes/obyn.png'

TOWER_NINJA_UPGRADE = 'resources/towers/ninja/upgrade_{}_{}.png'
TOWER_SUPER_UPGRADE = 'resources/towers/super/upgrade_{}_{}.png'

# Maps

# Dark Castle
MAPS_DARK_CASTLE = 'resources/maps/dark_castle/map.png'

POS_DARK_CASTLE_INTERSECTION_TOP = 'resources/maps/dark_castle/intersection_top_path.png'
POS_DARK_CASTLE_INTERSECTION_BOTTOM = 'resources/maps/dark_castle/intersection_bottom_path.png'
POS_DARK_CASTLE_TOP_LEFT_MAIN_ROAD = 'resources/maps/dark_castle/top_left_main_road.png'

ROUND_DARK_CASTLE_4 = 'resources/maps/dark_castle/round_4.png'
ROUND_DARK_CASTLE_20 = 'resources/maps/dark_castle/round_20.png'

# Hotkeys
HOTKEY_UPGRADE_1 = ','
HOTKEY_UPGRADE_2 = ';'
HOTKEY_UPGRADE_3 = ':'
HOTKEY_UPGRADES = [HOTKEY_UPGRADE_1, HOTKEY_UPGRADE_2, HOTKEY_UPGRADE_3]

HOTKEY_HERO = 'u'
HOTKEY_TOWER_NINJA = 'd'
HOTKEY_TOWER_SUPER_MONKEY = 's'
