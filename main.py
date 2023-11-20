from serialArduino import serialArduino
import yaml

# TODO:
# Convert to bits for more efficient transfer

# Load Lookup Table
with open('morse_code.yml', 'r') as file:
  conversion_table = yaml.safe_load(file)


# Farnsworth Timings
dit = '.'		# 1 unit
dah = '_'		# 3 units
intra = 'i'	# 1 unit
inter = 'j'	# 3 units
space = ' '	# 7 units

# Speed Control (Maybe put on a potentiometer?)
WPM = 1										# Words per minute (PARIS Standard)
t_unit = 60 / (50 * WPM)	# Seconds per unit


arduino = serialArduino()
arduino.initialize('/dev/cu.usbserial-120')
arduino.close()

