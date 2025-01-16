# in this file we

import os
import json


def get_parent_folder():
    current_directory = os.getcwd()  # get current working dir
    get_parent = os.path.dirname(current_directory)  # it will give the parent folder path
    return get_parent


def get_value_from_input_file(key):
    """
    it will fetch data form json file
    and it will pass the key as an argument and it will provide value for that key
    :param key:
    :return:
    """
    file_path = os.path.join(get_parent_folder(),"data","input.json")
    with open(file_path, "r")as file:
        data = json.load(file)
    return data[key].lower()
