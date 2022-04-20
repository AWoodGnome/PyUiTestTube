*** Settings ***
Documentation    PyUiTestingTube
...              A automatic ui testing pipeline
Library          keywords/robotkeywords.py

*** Test Cases ***
Write Hello World
    [Documentation]  Validation of basic functionality of a notepad
    Start Notepad
    Write Hello World
    Close Notepad