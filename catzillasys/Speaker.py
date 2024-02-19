import time
import serial
from rich.console import Console

console = Console()


class Speaker(object):

    def __init__(self, port="/dev/ttyUSB0", baudrate=9600, debug=False):
        self.SERIAL_PORT = port
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
            res = f"{status_message} on {self.SERIAL_PORT}! Baudrate={self.BAUDRATE}"
            console.print("[SUCCESS]", style="green bold", end=" ")
            console.print(f"{res}", style="bold")

    def close_serial(self):
        """
        Close the serial interface!
        """
        if self.serial.is_open:
            self.serial.close()
        if self.DEBUG:
            console.print("[SUCCESS]", end=" ", style="green bold")
            console.print("Serial port is now closed!")

    def is_open(self):
        return self.serial.is_open

    def write(self, message: str):
        """
        sends message/commands to the voice recognition device
        """
        message_bytes = message.encode()
        self.serial.write(message_bytes)
        if self.DEBUG:
            print(f"Data sent: {message_bytes}")

    def read(self):
        wait_count = self.serial.in_waiting
        if wait_count:
            data = self.serial.read()
            if self.DEBUG:
                print(f"Data read: {data}")
                return data


if __name__ == "__main__":
    speak = Speaker(port="COM3", baudrate=115200, debug=True)

    try:
        while True:
            speak.write("$A092#")
            time.sleep(5)
    except Exception as err:
        speak.close_serial()
        print(err)
