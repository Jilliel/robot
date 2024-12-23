from servo_control import PID
from controller import Controller

corrector = PID(kp=100, ki=10, kd=1)
ctl = Controller()
