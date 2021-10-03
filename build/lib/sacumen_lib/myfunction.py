import yaml
import configparser
import json

config = configparser.ConfigParser()

def conver_yml_to_dict(file_path):
    d = {}
    try:
        for key, val in yaml.load(open(file_path),Loader = yaml.SafeLoader).items():
            d[key] = val
    except FileNotFoundError as err:
        print('no file found')
        return  None

    return d

def convert_cfg_to_dict(file_path):
    try:
        config.read(file_path)
    except FileNotFoundError as err:
        print('File not found')
        return  None

    dictionary = {}
    for section in config.sections():
        dictionary[section] = {}
        for option in config.options(section):
            dictionary[section][option] = config.get(section, option)

    return dictionary

def get_dict(file_path):
    if str(file_path).endswith('yml'):
        return conver_yml_to_dict(file_path)

    elif str(file_path).endswith('cfg') or str(file_path).endswith('ini'):
        return convert_cfg_to_dict(file_path)


def convert_to_json(file_path, file_path_for_json):
    dictionary = None
    if str(file_path).endswith('yml') or str(file_path).endswith('yaml'):
        dictionary = conver_yml_to_dict(file_path)

    elif str(file_path).endswith('cfg') or str(file_path).endswith('ini'):
        dictionary = convert_cfg_to_dict(file_path)

    try:
        f = open(file_path_for_json, 'w')
    except:
        print('file not found')
        return None
    json.dump(dictionary, f, indent=4)
    f.close()
