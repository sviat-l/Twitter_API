"""
This module is created to provide navigation in json files

USAGE:
:go [key/index]  - go to the value on key/index
:gb - go back on 1 level
:gb / - go back to the root
:gb [number]  - go back on [number] > 0 levels
:print all - print all values from the root with their path from the root
:print - print all values from current location with their path from the root
:quit - stop running program
:h - print USAGE information
:crp - print current position from root
"""
import json


def navigate_json_file(path: str):
    """
    MAIN FUNCTION
    Parameters:
    :path - path to the json file
    Return : None
    """
    # define starting values
    data = get_data(path)
    key_stack = []
    current_data = data

    # print information about current location
    print_location_info(current_data, key_stack)
    while True:
        # get user input
        action = input('\n>>> ').split()
        # quit part
        if action[0].lower() == 'quit':
            break
        # help part
        if action[0].lower() in ['h', 'help']:
            print_help_info()
        # get part
        elif action == ['get']:
            print_location_info(current_data, key_stack)
        # print all values paths from the root part
        elif action == ['print', 'all']:
            print_path_info_from_root(data, [])
        # print current inner all paths part
        elif action == ['print']:
            print_path_info_from_root(current_data, key_stack)
        # print current path from the root
        elif action == ['crp']:
            value_print('', key_stack)
        # go / gb part,  handle errors
        else:
            try:
                # go part
                if action[0] == 'go' and len(action) == 2:
                    key_stack.append(get_key_from_input(current_data, action))
                # go back part
                elif action[0] == 'gb' and len(action) < 3:
                    key_stack = new_keys_stack(action, key_stack)
                # invalid input
                else:
                    raise ValueError
                # renew data
                current_data = renew_data(data, key_stack)
                print_location_info(current_data, key_stack)
            except ValueError:
                print("\nOops... WRONG INPUT! PLEASE FOLLOW THE RULES!\
                       \nIF YOU WANT SEE HELP INFORMATION PRINT: help")


def print_location_info(data: list | dict, key_stack: list) -> None:
    """
    Print information about current object . If it is a list then print number of indices.
    If it is a dictionary print available keys. If value is not a list or a dictionary - print it.
    Parameters:
    :data - current data list or dictionary with values
    :key_stack with consistent keys/indexes
    Return: None
    """
    # print position from the root
    value_print('', key_stack)
    # object case
    if isinstance(data, dict):
        print('Current value is an object. Available keys are:\n')
        [print(key) for key in data]
    # list case
    elif isinstance(data, list):
        print(f'Current value is a list with a length: {len(data)}')
    # value case
    else:
        print('There is a value:', data, sep=' ')


def get_key_from_input(data, action: list):
    """
    Return value(index or key) that will be added into a key_stack
    Parameters:
    :data - current data list or dictionary with values
    :action - list with user current action choice information
    Return:
    : key/index of the user choice
    """
    # main object list case
    if isinstance(data, list):
        index = int(action[1])
        if -1 < index < len(data):
            return index
    # main object dictionary case
    elif isinstance(data, dict):
        key = action[1]
        if key in data:
            return key
    # main object is value or key not in dictionary or index out of range
    raise ValueError


def new_keys_stack(action: list, key_stack: list) -> list:
    """
    Return new key_stack after cutting some last moves
    Parameters:
    :action - list with user current action choice information
    :key_stack with consistent keys/indexes
    Return:
    :key_stack - list with history of user key/index choices
    """
    # input : gb
    if len(action) == 1:
        return key_stack[:-1]
    # input: gb /
    if action[-1] == '/':
        return []
    # input format: gb [number]
    clear_number = int(action[1])
    if clear_number < 0:
        raise ValueError  # if clear_number < 0  or is not integer
    return key_stack[:-clear_number]


def renew_data(data: dict | list, key_stack: list) -> dict | list:
    """
    return new data on a location from the key_stack with consistent keys/indexes
    Parameters:
    :data - current data list or dictionary with values
    :key_stack with consistent keys/indexes
    Return:
    :new_data - data list or dictionary with values
    """
    new_data = data
    for key in key_stack:
        new_data = new_data[key]
    return new_data


def value_print(value, key_stack: list) -> None:
    """
    Print value information with path from the root
    Parameters:
    :value - str, int, float, bool or None value
    :key_stack with consistent keys/indexes
    Return: None
    """
    print(':'.join(['root'] + [f'[{x}]' if isinstance(x, int) else str(x) for x in key_stack]
                            + [str(value)]))


def print_path_info_from_root(data: dict | list, key_stack: list) -> None:
    """
    Print all values from current position and all elements of inner lists/objects
    Parameters:
    :data - current data list or dictionary with values
    :key_stack with consistent keys/indexes
    Return: None
    """
    if isinstance(data, list):
        for i, _ in enumerate(data):
            print_path_info_from_root(data[i], key_stack + [i])
    elif isinstance(data, dict):
        for key in data:
            print_path_info_from_root(data[key], key_stack + [key])
    else:
        value_print(data, key_stack)


def print_help_info() -> None:
    """print information about script usage"""
    print("USAGE:\n\
go [key/index]  - go to the value on key/index\n\
gb - go back on 1 level\n\
gb / - go back to the root\n\
gb [number]  - go back on [number] > 0 levels\n\
print all - print all values from the root with their path from the root\n\
print - print all values from current location with their path from the root\n\
quit - stop running program\n\
h - print USAGE information\n\
crp - print current position from root")


def get_data(path: str) -> list | dict:
    """ Open and decode json file
    Return all its information
    Parameters:
    :path - path to the json file
    Return : data with objects from file
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


WRITE_HERE_PATH_TO_THE_FILE = 'twitter2.json'
WRITE_HERE_PATH_TO_THE_FILE = '1_kved_parser/kved.json'
navigate_json_file(WRITE_HERE_PATH_TO_THE_FILE)
