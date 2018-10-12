# IRED mutlithreaded main file.

import IRED_utils
import IRED_ParseJson
import IRED_Logger
import time, traceback
import threading
import os
import json

if __name__ == "__main__":
 
    
    IRED_ParseJson.getDataFromConfig()
    #print json.dumps(IRED_ParseJson.CONFIG_DATA, indent=4)
    
    #IRED_Logger.openLogFile("./" + "Test_Execution_"+time.strftime("%y%m%d-%H%M%S") + ".log")
    IRED_Logger.setup_custom_logger()
    logger = IRED_Logger.get_logger_instance()

    #logger.info('main py file')

    # print ID of current process
    #print("ID of process running main program: {}".format(os.getpid()))
    logger.info("ID of process running main program: {}".format(os.getpid()))
    #IRED_Logger.printLog("ID of process running main program: {}".format(os.getpid()))
    # print name of main thread
    # print("Main thread name: {}".format(threading.main_thread().name))


    SCHEDULE = IRED_ParseJson.CONFIG_DATA
    c_interval = SCHEDULE["CaptureInterval"] * 60
    c_iter     = SCHEDULE["CaptureIterations"]
    c_duration = SCHEDULE["CaptureDuration"] * 60
    t_interval = SCHEDULE["TransferInterval"] * 60
    h_interval = SCHEDULE["HealthChkInterval"] * 60

    # creating threads
    t1 = threading.Thread(target=IRED_utils.captureVideoTask, name='t1_capture_task', args=(c_interval, c_iter, c_duration))
    t2 = threading.Thread(target=IRED_utils.sendVideoTask, name='t2_send_task', args=(t_interval,))  
    t3 = threading.Thread(target=IRED_utils.healthCheckTask, name='t3_healthCheck_task', args=(h_interval,))

# starting threads
    t1.start()
    time.sleep(2)
    t2.start()
    time.sleep(2)
    t3.start()
    time.sleep(2)
 
    # wait until all threads finish
    t1.join()
    t2.join()
    t3.join()

