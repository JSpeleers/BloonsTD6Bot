import pyautogui as pag
import cv2  # Needed for fuzzy matching with pyautogui
import logging
import time
from abc import ABCMeta, abstractmethod

import config


class Bot(metaclass=ABCMeta):

    def __init__(self):
        self._offset = (0, 0)
        self._monkeys_collection_path = None
        self._game_counter = 0
        self._wait_location = None
        pag.PAUSE = config.PYAUTOGUI_SLEEP_SECONDS_BETWEEN_CALLS
        config.init_logging()

    @property
    def wait_location(self):
        return self._wait_location

    # Clicks
    @staticmethod
    def _click_on(img):
        x = pag.locateCenterOnScreen(img, confidence=config.CLICK_ON_MATCHING_CONFIDENCE)
        if x is None:
            pag.screenshot('{}/debug_{}.png'.format(config.LOGS_DIR, time.time()))
            logging.error('Cannot find {} on screen'.format(img))
            raise ValueError('Cannot find {} on screen'.format(img))
        pag.click(x)

    @staticmethod
    def _place_hero_on_position(hero, position):
        x = pag.locateOnScreen(position)
        print('moving to ', x)
        pag.moveTo(x)
        pag.typewrite(hero)
        pag.click()

    def _start_level(self, fast_forward=True):
        self._click_on(config.BUTTON_START_LEVEL)
        if fast_forward:
            self._click_on(config.BUTTON_FAST_FORWARD)

    def _collect_event_rewards(self):
        logging.info('Collecting reward monkeys')
        for collection_x in config.COLLECTION_XS:
            pag.click((self._offset[0] + collection_x, self._offset[1] + config.COLLECTION_Y))
            pag.click((self._offset[0] + collection_x, self._offset[1] + config.COLLECTION_Y))
            if self._is_present(config.BUTTON_EVENT_CONTINUE):
                break
        self._monkeys_collection_path = '{}/collected_monkeys_{}.png'.format(config.LOGS_DIR, time.time())
        pag.screenshot(self._monkeys_collection_path)
        self._click_on(config.BUTTON_EVENT_CONTINUE)

    # Waits
    def wait_for(self, img):
        wait_counter = 0
        while not self._is_present(img):
            wait_counter += 1
            self._do_checks(wait_counter)

    def _wait_for_level_load(self):
        if self._is_present(config.PROMPT_OVERWRITE):  # Overwriting existing save
            logging.warning('Overwriting save')
            self._click_on(config.BUTTON_OVERWRITE_OK)
        self.wait_for(config.BUTTON_START_LEVEL)

    def _wait_for_level_completion(self):
        self.wait_for(config.BUTTON_LEVEL_TO_HOME)
        logging.info('Level has ended')
        self._click_on(config.BUTTON_LEVEL_TO_HOME)
        time.sleep(4)
        if self._is_present(config.BUTTON_EVENT_COLLECT):
            logging.info('Received reward monkeys')
            self._click_on(config.BUTTON_EVENT_COLLECT)
            self._collect_event_rewards()
            pag.press('esc')

    # Checks
    def _is_present(self, img):
        self._wait_location = pag.locateCenterOnScreen(img, confidence=config.WAIT_FOR_MATCHING_CONFIDENCE)
        return self._wait_location is not None

    @staticmethod
    def _check_reload(wait_counter):
        if wait_counter % config.RELOAD_TOWER_COUNTER == 0:
            logging.debug('Reloading')
            pag.click()
            pag.click()

    def _do_checks(self, wait_counter):
        self._check_level_up(wait_counter)
        self._check_game_paused(wait_counter)
        self._check_defeated(wait_counter)

    def _check_level_up(self, wait_counter):
        if wait_counter % config.CHECK_LEVEL_UP_COUNTER == 0 and self._is_present(config.PROMPT_LEVEL_UP):
            logging.warning('Level up detected - double clicking screen')
            pag.click()
            pag.click()
            self._check_game_paused(config.CHECK_GAME_PAUSED_COUNTER)

    def _check_game_paused(self, wait_counter):
        if wait_counter % config.CHECK_GAME_PAUSED_COUNTER == 0 and self._is_present(config.BUTTON_START_LEVEL):
            logging.warning('Game is paused detected - pressing play')
            self._start_level()

    def _check_defeated(self, wait_counter):
        if wait_counter % config.CHECK_DEFEATED_COUNTER == 0 and self._is_present(config.PROMPT_DEFEAT):
            logging.error('Defeat detected: starting new game')
            self.wait_for(config.BUTTON_LEVEL_TO_HOME)
            self._click_on(config.BUTTON_LEVEL_TO_HOME)
            self._game_counter -= 1
            self.main()
            exit(-1)

    # Main
    def main(self):
        logging.info('Bloons TD6 bot starting')
        logging.info('Please navigate to the top left corner of the game, you have {} seconds'.format(
            config.START_SLEEP_SECONDS))
        logging.debug('OpenCV loaded from {}'.format(cv2.data.haarcascades))
        time.sleep(config.START_SLEEP_SECONDS)
        self._offset = pag.position()
        logging.info('Screen offset set at {}'.format(self._offset))

        while True:
            self._game_counter += 1
            logging.info('---------------')
            logging.info('Starting game {}'.format(self._game_counter))
            initial_time = time.time()

            try:
                self._monkeys_collection_path = None
                self._play_game()
            except pag.FailSafeException:
                logging.info('Bot stopped at game {}.'.format(self._game_counter))
                exit(0)

            game_time = time.time() - initial_time
            logging.info(
                'Game {} has been completed in {} minutes {} seconds'.format(self._game_counter,
                                                                             int(game_time // 60),
                                                                             int(game_time % 60)))
            logging.info('{}'.format('Monkeys collected: {}'.format(
                self._monkeys_collection_path) if self._monkeys_collection_path else 'No monkeys collected.'))

    @abstractmethod
    def _play_game(self):
        pass  # Require implementation
