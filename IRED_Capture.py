# IRED camera capture module

import picamera
import time
import requests
import IRED_ParseJson
import IRED_Logger

def captureVideo(iteration = 1, duration = 60):
    logger = IRED_Logger.get_logger_instance() 
    # camera instance
    camera = picamera.PiCamera(sensor_mode=4, resolution='640x480', framerate=25)
    
    #camera.vflip = True
    #camera.hflip = True
    camera.brightness = 60
    
    PATH = IRED_ParseJson.CAPTURE_PATH
    for i in range(iteration):
        time_str = time.strftime("%Y%m%d-%H%M%S")
        logger.info ("Start capturing .... {}".format(PATH+'Vid%s.h264'%time_str))
        camera.start_recording(PATH+'Vid%s.h264' % time_str)
        time.sleep(duration)
        camera.stop_recording()
        logger.info ("Done ....")
    camera.close()

if __name__ == "__main__":
    captureVideo(2, 60)
