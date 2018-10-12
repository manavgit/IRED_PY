# IRED Client main file 

import IRED_utils
import time, traceback

def every(CaptureInterval, SendInterval,  task1, task2):
  c_time = time.time() + CaptureInterval
  s_time = c_time + SendInterval
  while True:
    time.sleep(max(0, c_time - time.time()))
    try:
      task1()
    except Exception:
      traceback.print_exc()

    time.sleep(max(0, (time.time() + (SendInterval - CaptureInterval)) - time.time()))
    try:
      task2()
    except Exception:
      traceback.print_exc()  

    # skip tasks if we are behind schedule:
    c_time += (time.time() - c_time) // CaptureInterval * CaptureInterval + CaptureInterval


every(5, 7, IRED_utils.captureVideo, IRED_utils.sendVideo)
