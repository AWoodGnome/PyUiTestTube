"""
Robot Listener
"""
import pprint
import RobotStackTracer


class RobotAdvancedListener:
    """
    Advanced Listener
    """
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        self.name = ""
        self.stack_trace = RobotStackTracer.RobotStackTracer()

    def start_suite(self, name, attrs):
        """
        Starting Suite
        """
        self.name = name
        pprint.pprint(f"{name} {attrs}")
        self.stack_trace.start_suite(name, attrs)

    def start_test(self, name, attrs):
        """
        start testcase
        """
        self.name = name
        self.stack_trace.start_test(name, attrs)
        pprint.pprint(f"{name} {attrs}")

    def start_keyword(self, name, attrs):
        """
        start keyword
        """
        self.name = name
        self.stack_trace.start_keyword(name, attrs)
        pprint.pprint(f"{name} {attrs}")

    def end_keyword(self, name, attrs):
        """
        end keyword
        """
        self.name = name
        self.stack_trace.end_keyword(name, attrs)
        pprint.pprint(f"{name} {attrs}")

    def end_test(self, name, attrs):
        """
        end test
        """
        self.name = name
        self.stack_trace.end_test(name, attrs)
        pprint.pprint(f"{name} {attrs}")

    def end_suite(self, name, attrs):
        """
        End Suite
        """
        self.name = name
        self.stack_trace.end_suite(name, attrs)
        pprint.pprint(f"{name} {attrs}")

    def library_import(self, name, attrs):
        """
        transfer to robot stack trace
        """
        self.stack_trace.library_import(name, attrs)

    def resource_import(self, name, attrs):
        """
        transfer to robot stack trace
        """
        self.stack_trace.resource_import(name, attrs)

    def log_message(self, message):
        """
        transfer to robot stack trace
        """
        self.stack_trace.log_message(message)

    def close(self):
        """
        Closing robot
        """
        print(f"closing {self.name}")
