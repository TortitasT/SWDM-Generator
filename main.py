import os
import sys
import loccli
import recorder
import time

data = loccli.GetData()

print("Get ready, in 3 seconds the program will open a window for recording, stay still while it finishes.")
time.sleep(3)
recorder.Record(data)