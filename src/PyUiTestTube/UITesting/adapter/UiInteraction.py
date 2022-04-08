"""Adapter functions using pywinauto"""
from common_functions.design_pattern import singleton


@singleton
class UiInteraction:
    """
    Adapter for sut interactions
    """

    def __init__(self):
        import logging

        self.app = None
        self.sut = None
        logging.basicConfig(level=logging.INFO)

    def key_typing(self, keys):
        """
        Native key type
        :param keys:
        """

        from pywinauto.keyboard import send_keys

        from common_functions.logging_functions import log
        send_keys(keys)
        log("Typing {}.".format(keys))

    def start_sut(self):
        """
        Starting software under test
        :return:
        """

        from pywinauto import application

        from common_functions.logging_functions import log
        from configuration.sut_config import sut_name
        self.app = application.Application()
        self.app.start(sut_name + '.exe')
        self.sut = self.app[sut_name]
        log("Sut {} started.".format(sut_name))

    def menu_select(self, menu: str):
        """
        Menu selecting
        :param menu:
        """

        from common_functions.logging_functions import log
        self.sut.menu_select(menu)
        log("Menu {} selected.".format(menu))

    def waiting(self, argument: str):
        """
        Waiting function
        :param argument:
        """

        from common_functions.logging_functions import log
        self.sut.wait(argument)
        log("Wait for {}.".format(argument))

    def writing(self, text: str):
        """
        Write into app
        :param text:
        """

        from common_functions.logging_functions import log
        self.sut['Edit'].set_edit_text(text)
        log("writing \n{}.".format(text))
