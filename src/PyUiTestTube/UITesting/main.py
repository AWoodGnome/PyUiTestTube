"""
Test automation main file
"""
import pprint

from pywinauto import application

from src.PyUiTestTube.UITesting.configuration.sut_config import sut_name


def main():
    app = application.Application()
    app.start(sut_name + '.exe')
    sut = app[sut_name]
    sut.wait('ready')
    sut.menu_select("Datei->Neu")
    sut['Edit'].set_edit_text(5 * "=" +
                              "\r\nHello world" +
                              5 * "=")
    app[sut_name + 'Dialog'].menu_select("Datei->Beenden")
    # Not save needs to be clicked
    sut['Edit'].print_control_identifiers()


if __name__ == '__main__':
    main()
