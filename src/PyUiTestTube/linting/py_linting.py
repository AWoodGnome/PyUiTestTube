"""
linting python files
"""
import os
import pylint


def get_py_files() -> list:
    """
    Get all py files
    """
    file_list = []
    os_walk_data = os.walk("../..")
    for item in os_walk_data:
        for name in item[2]:
            if '.py' in name and '.pyc' not in name and '__' not in name:
                file_list.append(os.path.join(item[0], name))
    return file_list


def main():
    """

    :return:
    """
    file_list = get_py_files()
    pylint.run_pylint(argv=file_list)


if __name__ == '__main__':
    main()
