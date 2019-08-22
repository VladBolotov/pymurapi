import threading
import zmq
import struct
from pymurapi import api


class Auv(api.MurApiBase, threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        api.MurApiBase.__init__(self)

        ctx = zmq.Context()
        self.unpacker = struct.Struct('=7f')
        self.packer = struct.Struct('=b8h3B2f')
        self.telemetry_socket = ctx.socket(zmq.SUB)
        self.control_socket = ctx.socket(zmq.PAIR)

    def get_image_front(self):
        print("get_image_front function works only in simulator.")
        return

    def get_image_bottom(self):
        print("get_image_bottom function works only in simulator.")
        return

    def run(self):
        while True:
            self._update()

    def prepare(self):
        telemetry_url = "tcp://127.0.0.1:2001"
        control_url = "tcp://127.0.0.1:2002"

        self.telemetry_socket.connect(telemetry_url)
        self.telemetry_socket.setsockopt_string(zmq.SUBSCRIBE, "")
        self.telemetry_socket.setsockopt(zmq.LINGER, 0)

        self.control_socket.connect(control_url)
        self.control_socket.setsockopt(zmq.SNDTIMEO, 3000)

        self.start()

    def _update(self):
        self.yaw, self.pitch, self.roll, self.depth, self.temperature, self.pressure, self.voltage = self.unpacker.unpack(
            self.telemetry_socket.recv())

        message = self.packer.pack(self.is_thrust_in_ms,
                                   self.motors_power[0],
                                   self.motors_power[1],
                                   self.motors_power[2],
                                   self.motors_power[3],
                                   self.motors_power[4],
                                   self.motors_power[5],
                                   self.motors_power[6],
                                   self.motors_power[7],
                                   self.colorRGB[0],
                                   self.colorRGB[1],
                                   self.colorRGB[2],
                                   self.on_delay,
                                   self.off_delay)

        self.control_socket.send(message)
