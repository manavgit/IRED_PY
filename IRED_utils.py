# IRED Utility Module

import time
import threading
import os
import IRED_HealthCheck
import IRED_Capture
import IRED_Transfer
import IRED_Logger
import IRED_ParseJson
import shutil

def ensureDir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def createDirectory():
    ensureDir(CAPTURE_PATH)
    ensureDir(LOGS_PATH)
    ensureDir(DEST_PATH)

def moveAllVideos():
    source = IRED_ParseJson.CAPTURE_PATH
    destination = IRED_ParseJson.DEST_PATH

    files = os.listdir(source)

    for file_name in files:
        shutil.move(source + file_name, destination)


def captureVideoTask(interval, iteration = 1, duration = 60):
  logger = IRED_Logger.get_logger_instance()
  logger.info("Task 1 assigned to thread: {}".format(threading.current_thread().name))
  logger.info("ID of process running to thread: {}".format(threading.current_thread().name))
  logger.info("Interval is - {}".format(interval))
  
  next_time = time.time() + interval
  while True:
    #time.sleep(max(0, next_time - time.time()))
    time.sleep(max(0, interval))
    try:
      IRED_Capture.captureVideo(iteration, duration)
      moveAllVideos()
    except Exception,ex:
      #traceback.logger.info_exc()
      logger.info("exception occured : {}".format(ex))
    # skip tasks if we are behind schedule:
    next_time += (time.time() - next_time) // interval * interval + interval

    

def sendVideoTask(interval):
  logger = IRED_Logger.get_logger_instance()
  logger.info("Task 2 assigned to thread: {}".format(threading.current_thread().name))
  logger.info("ID of process running task 2: {}".format(os.getpid()))
  logger.info("Interval is - {}".format(interval)) 
  
  next_time = time.time() + interval
  while True:
    time.sleep(max(0, interval))
    #time.sleep(max(0, next_time - time.time()))
    try:
      IRED_Transfer.sendVideo()
    except Exception,ex:
      #traceback.logger.info_exc()
      logger.info("exception occured : {}".format(ex))
    # skip tasks if we are behind schedule:
    next_time += (time.time() - next_time) // interval * interval + interval



def healthCheckTask(interval):
  logger = IRED_Logger.get_logger_instance()
  logger.info("Task 3 assigned to thread: {}".format(threading.current_thread().name))
  logger.info("ID of process running task 3: {}".format(os.getpid()))
  logger.info("Interval is - {}".format(interval)) 
  
  next_time = time.time() + interval
  while True:
    #time.sleep(max(0, next_time - time.time()))
    time.sleep(max(0, interval))
    try:
      d_status = IRED_HealthCheck.getDeviceStatus()
    except Exception,ex:
      #traceback.logger.info_exc()
      logger.info("exception occured : {}".format(ex))
    # skip tasks if we are behind schedule:
    next_time += (time.time() - next_time) // interval * interval + interval

