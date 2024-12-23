from collections import deque
import controller
from threading import Thread, Lock
from time import sleep

buffer = deque([])
ctl = controller.Controller()

def main():
    while True:
        if len(buffer) > 0:
            speed_l, speed_r = buffer.popleft()
            ctl.set_raw_motor_speed(speed_l, speed_r)
        sleep(0.1) #On marque une pause pour éviter de trop consommer le CPU
