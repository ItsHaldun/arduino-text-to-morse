import serial
from tabulate import tabulate
from serial.tools import list_ports
from typing import Union
from time import sleep

# TODO:
# Auto connect to official arduino
# Error Checking (Checksum, CRC)
# Length Byte for further error checking
# Start of message
# Packet number
# Escape Character
# Message number and storing the latest number
# Arduino being able to notice and request lost packages

class serialArduino:
  def __init__(self, connect_mode='Auto', encoding='utf-8'):
    self.available_ports = list_ports.comports()
    self.connect_mode = connect_mode
    self.encoding = encoding
    self.serial = None
    
    if self.available_ports == []:
      raise Exception("PORT ERROR: No available ports found!")
    else:
      print(f"\nAvailable devices:\n{tabulate(self.available_ports, headers=['Name','Desc','Hwid'], tablefmt='orgtbl')}\n")
  
  
  def initialize(self, port:str, baudrate:int=9600, timeout:float=1., reboot_timer:float=2.) -> None:
    # Check if desired port exists
    port_names = [port.device for port in self.available_ports]
    if port not in port_names:
      raise Exception(f"PORT ERROR: '{port}' is not a valid port name. Check serialArduino.available_ports for available ports")
    
    self.serial = serial.Serial(port, baudrate, timeout=timeout)
    sleep(reboot_timer)
    
    if self.serial.is_open:
      print(f"Serial connection to '{port}' has been initialized!")
    else:
      raise Exception(f"PORT ERROR: Connection to '{port}' is not open!")
  
  
  def read(self) -> str:
    # Connection Check
    if self.serial is None:
      raise Exception("PORT ERROR: Serial is not connected to a port")
    elif self.serial.is_open == False:
      raise Exception("PORT ERROR: Serial connection is not open")
    
    # Return the decoded message
    return self.serial.readline().decode(encoding=self.encoding)
  
  
  # Writes a given message to arduino serial as a line
  def write(self, msg: Union[str, int, float]) -> int:
    # Connection Check
    if self.serial is None:
      raise Exception("PORT ERROR: Serial is not connected to a port")
    elif self.serial.is_open == False:
      raise Exception("PORT ERROR: Serial connection is not open")
    # Returns the number of bytes written
    return self.serial.write(f'{msg}\n'.encode(encoding=self.encoding))

  
  def close(self) -> None:
    if self.serial.is_open:
      self.serial.close()
      print(f"Serial connection to port '{self.serial.port}' has been terminated")
    
    
  @property
  def baudrate(self):
    if self.serial is not None:
      return self.serial.baudrate
    else:
      return None
  
  @baudrate.setter
  def baudrate(self, new_rate):
    if self.serial is not None:
      self.serial.baudrate = new_rate
    else:
      raise Exception("PORT ERROR: Baudrate can't be set because serial port is not initialized!")
  
  @property
  def timeout(self):
    if self.serial is not None:
      return self.serial.timeout
    else:
      return None
  
  @timeout.setter
  def timeout(self, new_time):
    if self.serial is not None:
      self.serial.timeout = new_time
    else:
      raise Exception("PORT ERROR: Timeout can't be set because serial port is not initialized!")
  
  @property
  def port(self):
    if self.serial is not None:
      return self.serial.port
    else:
      return None
  
  @port.setter
  def port(self, new_port):
    if self.serial is not None:
      self.serial.port = new_port
    else:
      raise Exception("PORT ERROR: Port can't be set because serial port is not initialized!")

