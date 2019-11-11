import config
from bot import Bot
from tower import Tower


class DarkCastleBot(Bot):

    def __init__(self):
        Bot.__init__(self)

    # Single game
    def _play_game(self):
        self._click_on(config.BUTTON_PLAY)
        self._click_on(config.BUTTON_EXPERT_MAPS)
        self._click_on(config.MAPS_DARK_CASTLE)
        self._click_on(config.BUTTON_EASY_DIFF)
        self._click_on(config.BUTTON_STANDARD_MODE)

        self._wait_for_level_load()

        Tower(self, config.HOTKEY_HERO, config.POS_DARK_CASTLE_INTERSECTION_TOP, None, 'hero')

        self._start_level()

        self.wait_for(config.ROUND_DARK_CASTLE_4)

        ninja = Tower(self, config.HOTKEY_TOWER_NINJA, config.POS_DARK_CASTLE_INTERSECTION_BOTTOM,
                      config.TOWER_NINJA_UPGRADE, 'ninja')
        ninja.upgrade(1, 1)
        ninja.upgrade(3, 1)
        ninja.upgrade(1, 3)

        self.wait_for(config.ROUND_DARK_CASTLE_20)

        super_monkey = Tower(self, config.HOTKEY_TOWER_SUPER_MONKEY, config.POS_DARK_CASTLE_TOP_LEFT_MAIN_ROAD,
                             config.TOWER_SUPER_UPGRADE, 'super')
        super_monkey.upgrade(1, 2)
        super_monkey.upgrade(3, 2)

        self._wait_for_level_completion()


if __name__ == '__main__':
    bot = DarkCastleBot()
    bot.main()
