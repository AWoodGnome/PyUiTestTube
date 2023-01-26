# PyUiTestTube

## Description
PyUiTestTube should show a complete automated UI testing pipeline using open source components.  
The test object will be a notepad in which "Hello World" should be written.  
The complete pipeline consists out of these components:  
* Jenkins as continuous testing tool
* Robot Framework as keyword driven test scheduler
* PyWinAuto as adapter to the software under test

## Requirements
Make sure that your Python interpreter is in Path and C:\Project_PyUiTestTube\src\PyUiTestTube\UITesting is in PythonPath of the system environment.

## Robot Listener
To work with the Robot Advanced Listener correctly you need to add --quiet --listener Listener.robot_advanced_listener.RobotAdvancedListener to the arguments, you run Robot Framework.