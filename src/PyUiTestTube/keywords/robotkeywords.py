"""
Keywords for Robot Framework
"""
from adapter.ui_interaction import key_typing, UiInteraction
from test_data.text_data import TEST_TEXT


def close_notepad():
    """
    close notepad
    """
    sut = UiInteraction()
    sut.menu_select('Datei->Beenden')
    key_typing('{TAB}~')


def write_hello_world():
    """
    write the test_text
    """
    sut = UiInteraction()
    sut.menu_select('Datei->Neu')
    sut.writing(TEST_TEXT)


def start_notepad():
    """
    start notepad
    """
    sut = UiInteraction()
    sut.start_sut()
    sut.waiting('ready')
