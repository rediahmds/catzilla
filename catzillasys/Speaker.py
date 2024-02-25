"""
Module to interact with Speaker-Voice Recognition Module
"""

import time
import serial
from rich.console import Console

console = Console()


class Speaker:
  """
  Provides API to Speaker-Voice Recognition module.
  """

  def __init__(self, port="/dev/ttyUSB0", baudrate=9600, debug=False):
    """
    Instantiate and open serial connection with
    the Speaker-Voice Recognition module immediately.

    Args:
        `port` (`str`, optional): port name connected to the module. 
         Defaults to "/dev/ttyUSB0" in Ubuntu.
        `baudrate` (`int`, optional): baudrate value. It represents how many
         bits sent to the module per second. Defaults to 9600.
        `debug` (`bool`, optional): set debug mode on/off. 
        `True` means that debug mode is on. Defaults to False.
    """
    self.SERIAL_PORT = port
    self.DEBUG = debug
    self.BAUDRATE = baudrate
    self.open_serial()

  def open_serial(self):
    """
    Open serial connection in specified constructor argument.
    """
    # initializes serial interface on specific port and baudrate
    self.serial = serial.Serial(port=self.SERIAL_PORT, baudrate=self.BAUDRATE)

    # in debug mode, print info
    if self.DEBUG:
      status_message = (
          "Speech Serial port successfully opened"
          if self.serial.is_open
          else "Speech Serial port failed to open"
      )
      status = (
        f"{status_message} on {self.SERIAL_PORT}! Baudrate={self.BAUDRATE}"
      )
      console.print("[SUCCESS]", style="green bold", end=" ")
      console.print(f"{status}", style="bold")

  def close_serial(self):
    """
    Close the serial interface.
    """
    if self.serial.is_open:
      self.serial.close()
    if self.DEBUG:
      console.print("[SUCCESS]", end=" ", style="green bold")
      console.print("Serial port is now closed!")

  def is_open(self):
    """
    Check if serial port is open
    Returns:
        `bool`: `True` means the port is opened.
    """
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
    """
    Read data sent by Speaker-Voice Recognition module.
    """
    wait_count = self.serial.in_waiting
    if wait_count:
      data = self.serial.read()
      if self.DEBUG:
        print(f"Data read: {data}")
        return data

  def send_command_test(self, command="$A087#"):
    """
    Test to send command

    Args:
        `command` (`str`, optional): _description_. Defaults to "$A087#".
    """
    try:
      if not self.is_open:
        self.open_serial()

      while True:
        self.write(command)
        time.sleep(3)

    except KeyboardInterrupt as keyboard_interrupt_err:
      self.close_serial()
      console.print(keyboard_interrupt_err, style="red")


if __name__ == "__main__":
  speaker = Speaker(baudrate=115200, debug=True)
  speaker.send_command_test()
