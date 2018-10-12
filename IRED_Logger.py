# IRED logger module
import logging
import os
import time
import IRED_ParseJson
import sys

logger = 0
file = 0
LogDir = os.getcwd()+"/Logs/"

def setup_custom_logger():
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    filename = get_file_name()
    #print ("Filename path is {}".format(filename))
    handler = logging.FileHandler(LogDir+filename, mode = 'w', encoding=None, delay = False)
    handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    
    global logger
    logger = logging.getLogger('logger')
    logger.setLevel(logging.INFO)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(stream_handler)
    return logger

def get_logger_instance():
    return logger

def get_file_name():
    file_name = ""
    #print(IRED_ParseJson.CONFIG_DATA)
    base_file_name = IRED_ParseJson.DEFAULT_CONFIG_DATA["DeviceID"] 
    current_log_file_name = time.strftime(base_file_name + "_%y%m%d" + ".log")
    
    log_files = os.listdir(LogDir)

    if len(log_files) == 0:
        file_name = current_log_file_name
        return file_name

    for name in log_files:
        if name.endswith(".log") and name == current_log_file_name :
            #something do
            file_name = name
        else:
            file_name = current_log_file_name
    return file_name

def openLogFile(str):
    global file
    file = open(str, 'w')

def printLog(str):
    if file == 0:
       print "File is not available to write ..!"
    else:
       file.write(str+"\n")

def closeLogFile():
    printLog("Closing file .... !")
    file.close()

if __name__ == "__main__":
    
    openLogFile("./test_log.txt")
    printLog("Hello world")
    closeLogFile()

    
