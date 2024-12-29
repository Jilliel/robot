import controller
from collections import deque
from threading import Thread, Lock


class Motors:
    def __init__(self):
        self.motor_buffer = deque([])
        self.motor_buffer_lock = Lock()

        self.motor_ctl = controller.Controller()
        self.motor_ctl.set_motor_shutdown_timeout(5)

        self.motor_thread = Thread(target=self.main)
        self.motor_thread.run()

    def main(self):
        """
        Donne une consigne au moteur
        """
        while True: 
            with self.motor_buffer_lock:
                if len(self.motor_buffer) > 0:
                    speed_l, speed_r = self.motor_buffer.popleft()
                else:
                    speed_l, speed_r = 0, 0
            self.motor_ctl.set_raw_motor_speed(speed_l, speed_r)
