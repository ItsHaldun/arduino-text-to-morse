from serialArduino import serialArduino
import morse

# TODO:
# Convert to bits for more efficient transfer
# Test buffer reset on arduino
# Speed control using potentiometer (Use INTERRUPTS!)
# MILIS INSTEAD OF DELAY (DELAY IS BLOCKING)
# Extra logic for buffer reset?


arduino = serialArduino()
arduino.initialize('/dev/cu.usbserial-140')


exitRecieved = False
exitCode = 'exit'

print(f"Press enter to send morse code. Type '{exitCode}' to exit.")
while not exitRecieved:
  msg = input("Enter: ")
  
  if msg == exitCode:
    confirm =  ''
    while confirm not in ['y', 'n']:
      confirm = input("Do you want to exit (y/n): ")
    if confirm == 'y':
      exitRecieved = True
      continue
  
  print(f"Morse: {morse.text_to_morse(msg)}")
  morse_msg = morse.text_to_farnsworth(msg)
  print(f"DEBUG: {morse_msg}")
  arduino.write(morse_msg)

arduino.close()