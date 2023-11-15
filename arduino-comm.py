import serial
from tabulate import tabulate
from serial.tools import list_ports
from typing import Union
from time import sleep

class serialArduino:
  def __init__(self):
    self.ports = list_ports.comports()
    self.serial = None
    print(f"\nAvailable devices:\n{tabulate(self.ports, headers=['Name','Desc','Hwid'], tablefmt='orgtbl')}\n")
  
  
  def initialize(self, port:str, baudrate:int=9600, timeout:float=1.) -> None:
    # Check if desired port exists
    available_ports = [port.device for port in self.ports]
    if port not in available_ports:
      raise Exception(f"PORT ERROR: '{port}' is not a valid port name. Check serialArduino.ports for available ports")
    
    self.serial = serial.Serial(port, baudrate, timeout=timeout)
    
    if self.serial.is_open:
      print(f"Serial connection to '{port}' has been initialized!")
    else:
      raise Exception(f"PORT ERROR: Connection to '{port}' is not open!")
  
  
  def read(self):
    return self.serial.readline()
  
  
  # Writes a given message to arduino serial as a line
  def write(self, msg: Union[str, int, float]):
    self.serial.write(b'{msg}\n')
  
  
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




if __name__ == "__main__":
  arduino = serialArduino()
  arduino.initialize('/dev/cu.usbserial-120')
  arduino.write('g')
  
  i = 0
  while (i<10):
    arduino.write('g')
    sleep(1)
    i+=1
  
  arduino.close()