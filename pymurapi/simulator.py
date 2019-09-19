import threading
import zmq
import cv2
import struct
import time
import numpy as np
from pymurapi import api


class Simulator(api.MurApiBase, threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        api.MurApiBase.__init__(self)

        ctx = zmq.Context()
        self.unpacker = struct.Struct('=8b7f')
        self.packer = struct.Struct('=4b')
        self.front_socket = ctx.socket(zmq.SUB)
        self.bottom_socket = ctx.socket(zmq.SUB)
        self.mcu_socket = ctx.socket(zmq.SUB)
        self.motors_socket = ctx.socket(zmq.PAIR)
        self.front_image = np.zeros((240, 320, 3), np.uint8)
        self.bottom_image = np.zeros((240, 320, 3), np.uint8)

    def get_image_front(self):
        return self.front_image

    def get_image_bottom(self):
        return self.bottom_image

    def run(self):
        while True:
            self._update()
            time.sleep(0.001)

    def prepare(self):
        bottom_image_url = "tcp://127.0.0.1:1771"
        front_image_url = "tcp://127.0.0.1:1772"
        mcu_url = "tcp://127.0.0.1:3390"
        motors_url = "tcp://127.0.0.1:3391"

        self.front_socket.connect(front_image_url)
        self.front_socket.setsockopt(zmq.LINGER, 0)
        self.front_socket.setsockopt_string(zmq.SUBSCRIBE, "")

        self.bottom_socket.connect(bottom_image_url)
        self.bottom_socket.setsockopt(zmq.LINGER, 0)
        self.bottom_socket.setsockopt_string(zmq.SUBSCRIBE, "")

        self.mcu_socket.connect(mcu_url)
        self.mcu_socket.setsockopt(zmq.LINGER, 0)
        self.mcu_socket.setsockopt_string(zmq.SUBSCRIBE, "")

        self.motors_socket.connect(motors_url)
        self.motors_socket.setsockopt(zmq.SNDTIMEO, 3000)

        self.start()

    def _update(self):
        front_image_jpg = np.fromstring(self.front_socket.recv(), dtype='uint8')
        bottom_image_jpg = np.fromstring(self.bottom_socket.recv(), dtype='uint8')
        _, _, _, _, _, _, _, _, pitch, roll, yaw, depth, _, _, _ = self.unpacker.unpack(self.mcu_socket.recv())

        msg = self.packer.pack(self.motors_power[0], self.motors_power[1], self.motors_power[2], self.motors_power[3])
        self.motors_socket.send(msg)

        self.front_image = cv2.imdecode(front_image_jpg, 1)
        self.bottom_image = cv2.imdecode(bottom_image_jpg, 1)
        self.pitch = pitch
        self.roll = roll
        self.yaw = yaw
        self.depth = depth
