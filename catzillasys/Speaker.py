import serial
import time


class Speech(object):

    def __init__(self, com="/dev/ttyUSB0", baudrate=9600, debug=False):
        self.SERIAL_PORT = com
        self.DEBUG = debug
        self.BAUDRATE = baudrate
        self.open_serial()

    def open_serial(self):
        # initializes serial interface on specific port and baudrate
        self.serial = serial.Serial(port=self.SERIAL_PORT, baudrate=self.BAUDRATE)

        # in debug mode, print info
        if self.DEBUG:
            status_message = (
                "Speech Serial port successfully opened"
                if self.serial.is_open
                else "Speech Serial port failed to open"
            )
            print(f"{status_message} on {self.SERIAL_PORT}! Baudrate={self.BAUDRATE}")

    def close_serial(self):
        """
        Close the serial interface!
        """
        if self.serial.is_open:
            self.serial.close()
        if self.DEBUG:
            print(f"Speech Serial port Closed!")

    def is_open(self):
        return self.serial.is_open

    def write(self, message: str):
        """
        sends message/commands to the voice recognition device
        """
        message_bytes = message.encode()
        self.serial.write(message_bytes)

    def read(self):
        return self.serial.read()


if __name__ == "__main__":
    speak = Speech(com="COM10", baudrate=115200, debug=True)

    try:
        while True:
            speak.write("$A092#")
            time.sleep(5)
    except KeyboardInterrupt:
        speak.close_serial()
