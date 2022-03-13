"""Adapter functions using pywinauto"""
import logging

from pywinauto import application
from pywinauto.keyboard import send_keys

from src.PyUiTestTube.UITesting.common_functions.logging_functions import log
from src.PyUiTestTube.UITesting.configuration.sut_config import sut_name


def key_typing(keys):
    """
    Native key type
    :param keys:
    """
    send_keys(keys)
    log("Typing {}.".format(keys))


class SutAdapter:
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
        self.app.start(sut_name + '.exe')
        self.sut = self.app[sut_name]
        log("Sut {} started.".format(sut_name))

    def menu_select(self, menu: str):
        """
        Menu selecting
        :param menu:
        """
        self.sut.menu_select(menu)
        log("Menu {} selected.".format(menu))

    def waiting(self, argument: str):
        """
        Waiting function
        :param argument:
        """
        self.sut.wait(argument)
        log("Wait for {}.".format(argument))

    def writing(self, text: str):
        """
        Write into app
        :param text:
        """
        self.sut['Edit'].set_edit_text(text)
        log("writing \n{}.".format(text))
