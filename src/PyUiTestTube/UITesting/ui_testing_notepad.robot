*** Settings ***
Documentation    PyUiTestingTube
...              A automatic ui testing pipeline
Library          keywords/robotkeywords.py

*** Test Cases ***
Write Hello World
    Start Notepad
    Write Hello World
    Close Notepad