from typing import Union
import yaml

# Load Lookup Table
with open('morse_code.yml', 'r') as file:
  conversion_table = yaml.safe_load(file)
  keys = list(conversion_table.keys())

# Farnsworth Timings
dit = '.'		# 1 unit
dah = '_'		# 3 units
intra = 'i'	# 1 unit
inter = 'j'	# 3 units
space = ' '	# 7 units


def text_to_morse(text: Union[str, int], strict=False) -> str:
  # Check for correct type
  if type(text) not in [str, int]:
    raise TypeError(f"{text} is not of type str, int or float")
  
  # Cast to proper form
  text = str(text).upper()
  
  morse = ""
  for c in text:
    if c not in keys:
      if c == ' ':
        morse += '/ '
      else:
        if strict:
          raise KeyError(f"{c} is not in morse table")
    else:
      morse += conversion_table[c]
      morse += ' '
  return morse

def text_to_farnsworth(text: Union[str, int], strict=False) -> str:
  # Check for correct type
  if type(text) not in [str, int]:
    raise TypeError(f"{text} is not of type str, int or float")
  
  # Cast to proper form
  text = str(text).upper()
  
  farnsworth = ""
  for c in text:
    if c not in keys:
      if c == space:
        farnsworth += c
      else:
        if strict:
          raise KeyError(f"{c} is not in morse table")
    else:
      morse = conversion_table[c]
      farnsworth += "".join(i + j for i, j in zip(morse, intra*len(morse)))
    if c != space:
      farnsworth += inter
  return farnsworth