import re
import argparse

def parse_log(log_string):
  # Define the regular expression pattern for the log format
  pattern = r'(\d+\.\d+\.\d+\.\d+)\s-\s-\s\[(.+)\]\s"(.+)"\s(\d+)\s(\d+)\s"(.+)"\s"(.+)"'

  # Compile the regular expression
  regex = re.compile(pattern)

  # Split the log string into individual lines
  lines = log_string.split('\n')

  # Initialize a list to store the parsed log entries
  log_entries = []

  # Iterate over each line in the log string
  for line in lines:
    # Try to match the line with the regular expression
    match = regex.match(line)
    if match:
      # If the line matches the pattern, extract the relevant information
      ip_address = match.group(1)
      timestamp = match.group(2)
      request = match.group(3)
      status_code = match.group(4)
      bytes_sent = match.group(5)
      referrer = match.group(6)
      user_agent = match.group(7)

      # Create a dictionary for the log entry
      log_entry = {
          'ip_address': ip_address,
          'timestamp': timestamp,
          'request': request,
          'status_code': status_code,
          'bytes_sent': bytes_sent,
          'referrer': referrer,
          'user_agent': user_agent
      }

      # Add the log entry to the list
      log_entries.append(log_entry)

  return log_entries

def main():
  # Parse the command line arguments
  parser = argparse.ArgumentParser()
  parser.add_argument('log_file', help='the log file to parse')
  args = parser.parse_args()

  # Read the log file
  with open(args.log_file, 'r') as f:
    log_string = f.read()

  # Parse the log file
  log_entries = parse_log(log_string)

  # Print the log entries
  for entry in log_entries:
    print(entry)

if __name__ == '__main__':
  main()
