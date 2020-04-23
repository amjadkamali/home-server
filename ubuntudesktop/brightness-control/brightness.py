#!/usr/bin/env python3

import os

# Set Monitor SN for reading brightness
monitorSN=""
# Set the increment between each brightness step
increment=5

# This will show up as the status icon
print("🌞\n---")

# Read the brightness from the monitor and format it so we only get the number itself
currentBrightness = str(os.popen("ddcutil --sn={0} getvcp 0x10 | grep -o -E '[0-9]+' | sed -n '3p'".format(monitorSN)).read())

# Convert the output to an integer or set it to -1 if we got some other output
currentBrightness = int(currentBrightness) if currentBrightness else -1

# Loop through each increment 
for step in range(int(100/increment)+1):
  # Set the actual brightness
  brightness=(step*increment)
  # Set the icon to starred for all steps up to the current brightness
  iconName='starred' if brightness<=currentBrightness else 'non-starred'
  # This the line that argos forms a clickable action with
  print("{0} | bash='ddcutil setvcp 0x10 {0}' refresh=true terminal=false iconName={1}".format(brightness,iconName))

print('---\nColor Temperature:')
for x in [["6500K", "0x05"],["Custom", "0x0b"]]:
  print("{} | bash='ddcutil setvcp 14 {}' terminal=false".format(*x))

