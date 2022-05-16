import os
import time
ip = input("IP To Ddos:")
os.system("ping {} -n 10000".format(ip))
time.sleep("100000") ##for no close.
