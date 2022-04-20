"""
Singleton design pattern
"""


def singleton(class_):
    """
    :param class_:
    :return:
    """
    instances = {}

    def getinstance(*args, **kwargs):
        """
        getting instance
        """
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance
