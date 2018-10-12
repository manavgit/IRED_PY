# IRED json file parsing module

import json
import os
import os.path

CONFIG_PATH='./config.txt'
CAPTURE_PATH = './Vid/'
DEST_PATH = './MovedVid/'

DEFAULT_CONFIG_DATA = {
    "DeviceID"          : "IREDRPI001",
    "AreaCode"          : "PH1MOHCHD",
    "CaptureInterval"   : 60,
    "CaptureIterations" : 3,
    "CaptureDuration"   : 1,
    "TransferInterval"  : 180,
    "HealthChkInterval" : 30,
    "TotalCycle"        : 4, 
}

CONFIG_DATA = {}

def readJsonFile(fileName):
    with open(fileName) as json_file: 
        data = json.load(json_file)
    return data

def getDataFromConfig():
    if os.path.isfile(CONFIG_PATH) and os.access(CONFIG_PATH, os.R_OK):
        data = readJsonFile(CONFIG_PATH)
        #print(data)
    else:
        global CONFIG_DATA
        print ("IRED_DataStruc :: getDataFromConfig ERROR : cannot find the file - {} !!!".format(fileName))
        global CONFIG_DATA
    if len(data) == 0:
        CONFIG_DATA = DEFAULT_CONFIG_DATA
    else:    
        CONFIG_DATA = dict(data)
    #print json.dumps(CONFIG_DATA, indent=4)

#getDataFromConfig()


