"""
Test automation main file
"""
import logging

from src.PyUiTestTube.UITesting.adapter.adapter_pywinauto import SutAdapter, key_typing
from src.PyUiTestTube.UITesting.test_data.test_data import test_text


def main():
    """
    Main script for testing
    """
    logging.basicConfig(level=logging.INFO)
    sut = SutAdapter()
    sut.start_sut()
    sut.waiting('ready')
    sut.menu_select('Datei->Neu')
    sut.writing(test_text)
    sut.menu_select('Datei->Beenden')
    key_typing('{TAB}~')


if __name__ == '__main__':
    main()
