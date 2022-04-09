"""
Linting robot files
"""
import os
import subprocess

import rflint

def get_py_files() -> list:
    """
    Get all robot files
    """
    file_list = []
    os_walk_data = os.walk("..")
    for item in os_walk_data:
        for name in item[2]:
            if '.robot' in name:
                file_list.append(os.path.join(item[0], name))
    return file_list


def validate_files(file_list: list):
    for file in file_list:
        subprocess.run(f"rflint {file}")


def main():
    """
    Validate robot framework files with rf lint
    """
    file_list = get_py_files()
    validate_files(file_list)


if __name__ == '__main__':
    main()
