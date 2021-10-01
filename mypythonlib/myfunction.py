import json


import yaml
from yaml.loader import SafeLoader

with open("config.json") as json_data_file:
    data = json.load(json_data_file)
print("JSON File:-",data)


with open("config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile,Loader=SafeLoader)

print("YAML File:-",cfg)


# Load the configuration file
with open("config.ini") as f:
    sample_config = f.read()

print("INI file:-",sample_config)


with open("config.xml") as f:
    content = f.read()

print("XML file:-",content)

