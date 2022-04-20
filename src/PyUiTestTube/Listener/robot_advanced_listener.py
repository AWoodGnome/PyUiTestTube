"""
Robot Listener
"""
import pprint
import RobotStackTracer
from robot.api import logger


def parse_to_table(attrs):
    """
    Parsing attrs to log_string
    """
    #print.pprint(attrs)
    if 'longname' in attrs:
        name = attrs['longname']
    elif 'kwname' in attrs:
        name = attrs['kwname']
    elif 'originalname' in attrs:
        name = attrs['originalname']
    else:
        pprint.pprint(attrs)
        name = "==?="
    start_time = ""
    if 'starttime' in attrs:
        start_time = attrs['starttime']
    end_time = ""
    if 'endtime' in attrs:
        end_time = attrs['endtime']
    n = 0
    column_width = [50, 8, 8]
    for variable in [name, start_time, end_time]:
        variable_length = len(variable)
        if variable_length <= column_width[n]:
            variable += (column_width[n] - variable_length) * " "
            print((column_width[n] - variable_length))
        else:
            variable = variable[:column_width[n]]
        n +=1

    log_string = f"{name} {start_time} {end_time}"
    return log_string

def write_to_console(attrs):
    """
    Write to console
    """
    log_string = parse_to_table(attrs)
    logger.console(log_string)


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
        self.stack_trace.start_suite(name, attrs)
        write_to_console(attrs)

    def start_test(self, name, attrs):
        """
        start testcase
        """
        self.name = name
        self.stack_trace.start_test(name, attrs)
        write_to_console(attrs)

    def start_keyword(self, name, attrs):
        """
        start keyword
        """
        self.name = name
        self.stack_trace.start_keyword(name, attrs)
        write_to_console(attrs)

    def end_keyword(self, name, attrs):
        """
        end keyword
        """
        self.name = name
        self.stack_trace.end_keyword(name, attrs)
        write_to_console(attrs)

    def end_test(self, name, attrs):
        """
        end test
        """
        self.name = name
        self.stack_trace.end_test(name, attrs)
        write_to_console(attrs)

    def end_suite(self, name, attrs):
        """
        End Suite
        """
        self.name = name
        self.stack_trace.end_suite(name, attrs)
        write_to_console(attrs)

    def library_import(self, name, attrs):
        """
        transfer to robot stack trace
        """
        self.stack_trace.library_import(name, attrs)
        write_to_console(attrs)

    def resource_import(self, name, attrs):
        """
        transfer to robot stack trace
        """
        self.stack_trace.resource_import(name, attrs)
        write_to_console(attrs)

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
