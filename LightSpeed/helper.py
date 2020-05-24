import json, os


def writeConfigToFile(config):
    with open('config.json', 'w') as outfile:
        json.dump(config, outfile)


def readConfigFile():
    if not os.path.exists('config.json'):
        config = {}
        config['message'] = 'File not found'
        return config

    with open('config.json') as json_file:
        config = json.load(json_file)
        return config
