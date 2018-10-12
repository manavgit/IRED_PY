# IRED video tranfer module

import IRED_ParseJson
import IRED_Logger
import requests
from requests_toolbelt import MultipartEncoder
import os
import time

url = 'http://52.224.66.188/ImageAPI/api/PostImage'

def transferVideoToServer(videoFileStr):
    logger = IRED_Logger.get_logger_instance() 
    m = MultipartEncoder(fields={'field2': (videoFileStr, open(IRED_ParseJson.DEST_PATH+videoFileStr, 'rb'), 'video/mp4')})
    response = requests.post(url,data = m, headers={'Content-Type': m.content_type} )
    
    logger.info(response.status_code)
    logger.info(response.content)
    logger.info(response.headers)

    return (response.status_code, response.content)


def sendVideo():
    logger = IRED_Logger.get_logger_instance() 
    logger.info("--- Using os.listdir ---")
    n = 0
    files = os.listdir(IRED_ParseJson.DEST_PATH)
    for fn in files:
        if fn.endswith('.h264'):
            n += 1
            logger.info(fn)
            status_code, content = transferVideoToServer(fn)
            time.sleep(1)
            if content.find("SUCCESS") != -1:
                logger.info ("Remove file at path - {}".format(IRED_ParseJson.DEST_PATH+fn))
                os.remove(IRED_ParseJson.DEST_PATH+fn)

    logger.info("count = {}".format(n))


if __name__ == "__main__":
    sendVideo()
