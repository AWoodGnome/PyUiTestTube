"""Adapter functions using pywinauto"""
import logging

from pywinauto.keyboard import send_keys
from pywinauto import application

from common_functions.design_pattern import singleton
from common_functions.logging_functions import log
from configuration.sut_config import SUT_NAME


def key_typing(keys):
    """
    Native key type
    :param keys:
    """

    send_keys(keys)
    log(f"Typing {keys}.")


@singleton
class UiInteraction:
    """
    Adapter for sut interactions
    """

    def __init__(self):

        self.app = None
        self.sut = None
        logging.basicConfig(level=logging.INFO)

    def start_sut(self):
        """
        Starting software under test
        :return:
        """

        self.app = application.Application()
        self.app.start(SUT_NAME + '.exe')
        self.sut = self.app[SUT_NAME]
        log(f"Sut {SUT_NAME} started.")

    def menu_select(self, menu: str):
        """
        Menu selecting
        :param menu:
        """

        self.sut.menu_select(menu)
        log(f"Menu {menu} selected.")

    def waiting(self, argument: str):
        """
        Waiting function
        :param argument:
        """

        self.sut.wait(argument)
        log(f"Wait for {argument}.")

    def writing(self, text: str):
        """
        Write into app
        :param text:
        """

        self.sut['Edit'].set_edit_text(text)
        log(f"writing \n{text}.")
