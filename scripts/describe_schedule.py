# This script parses the given config file and prints a human readable description of the schedule to the command line.

import sys
import json

# Get file name.
file_name = sys.argv[1]
print(f'Describing config from "{file_name}"')
print()

# Load JSON.
with open(file_name,'r') as fp:
  config = json.load(fp)

# Describe config name.
config_name = config['name']
print(f"Config name: {config_name}")
print()

# Loop through days of the week.
for day in ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']:

  # Check if day is in schedule.
  if day in config['schedule']:

    # Get schedule.
    schedule = config['schedule'][day]
    
    # Get sorted list of times.
    times = sorted(config['schedule'][day].keys())
    
    # Introduce day.
    print(f'On {day}, the schedule is as follows:')

    # Loop through times and describe.
    for time in times:
      temp = schedule[time]
      print(f'The heating will be set to {temp}C at {time}')

    # Add blank line for readability.
    print()

  else:

    # No schedule for the day.
    print(f'On {day}, no schedule has been defined.')

  # Add blank line for readability.
  print()
