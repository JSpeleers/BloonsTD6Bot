import logging

import config
from bot import Bot


class Map:

    def __init__(self, name):
        self._name = name

    def _log_navigation(self):
        logging.info('Navigating to map {}'.format(self._name))


class DarkCastleMap(Map):

    def __init__(self):
        super().__init__('Dark Castle')

    def navigate_to(self):
        self._log_navigation()
        Bot.click_on(config.BUTTON_MENU_PLAY)
        Bot.click_on(config.BUTTON_MENU_MAPS_EXPERT)
        Bot.click_on(config.MAPS_DARK_CASTLE)
        Bot.click_on(config.BUTTON_MENU_EASY_DIFF)
        Bot.click_on(config.BUTTON_MENU_STANDARD_MODE)
