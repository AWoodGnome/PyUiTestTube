"""
Keywords for Robot Framework
"""


def close_notepad():
    """
    close notepad
    """
    from adapter.UiInteraction import UiInteraction
    sut = UiInteraction()
    sut.menu_select('Datei->Beenden')
    sut.key_typing('{TAB}~')


def write_hello_world():
    """
    write the test_text
    """
    from adapter.UiInteraction import UiInteraction
    from test_data.test_data import test_text
    sut = UiInteraction()
    sut.menu_select('Datei->Neu')
    sut.writing(test_text)


def start_notepad():
    """
    start notepad
    """
    from adapter.UiInteraction import UiInteraction
    sut = UiInteraction()
    sut.start_sut()
    sut.waiting('ready')