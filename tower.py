import pyautogui as pag
import logging

import config


class Tower:
    def __init__(self, bot, hotkey, position, upgrade_path, name='tower'):
        self.name = name
        self.bot = bot
        self.bot.wait_for(position)
        self.position = self.bot.wait_location
        self.hotkey = hotkey
        self.upgrades = [0, 0, 0]
        self.upgrade_path = upgrade_path
        logging.info('Placing {}'.format(self.name))
        pag.moveTo(self.position)
        pag.typewrite(self.hotkey)
        pag.click()

    @staticmethod
    def _upgrade_track(track):
        pag.press(config.HOTKEY_UPGRADES[track - 1])

    def _tower_upgrades_to_string(self, track, to_level):
        string = ''
        for i, upgrade_level in enumerate(self.upgrades):
            string += str(to_level) if i + 1 == track else str(upgrade_level)
        return string

    def upgrade(self, track, to_level):
        if track > 3 or to_level > 5:
            logging.error('Track ({}) or level ({}) is too high'.format(track, to_level))
            raise ValueError('Track ({}) or level ({}) is too high'.format(track, to_level))
        pag.click(self.position)
        for i in range(to_level - self.upgrades[track - 1]):
            logging.info('Waiting for {} {}'.format(self.name, self._tower_upgrades_to_string(track, i + 1)))
            self.bot.wait_for(self.upgrade_path.format(track, self.upgrades[track - 1] + i + 1), reload=True)
            self._upgrade_track(track)
        self.upgrades[track - 1] = to_level
        pag.click(self.position)
