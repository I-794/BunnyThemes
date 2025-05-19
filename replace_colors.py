import json
import random
import re
import argparse

def random_hex_color():
  """Generates a random hex color code."""
  return "#{:06x}".format(random.randint(0, 0xFFFFFF)).upper() # Ensure uppercase hex

def replace_colors_in_file(filepath):
  """Reads a JSON file, replaces hex color codes, and writes back."""
  try:
    with open(filepath, 'r') as f:
      content = f.read()
  except FileNotFoundError:
    print(f"Error: File not found at {filepath}")
    return False # Indicate failure

  # Regex for quoted hex strings like "#AABBCC"
  # It ensures the # is followed by exactly 6 hex characters (case-insensitive)
  # and that the entire thing is enclosed in double quotes.
  hex_color_regex = r"\"#(?:[0-9a-fA-F]{6})\""

  def replacer(match):
    original_text = match.group(0)
    # Check if the matched string (including quotes) is "transparent"
    # This check might be too simplistic if "transparent" can appear in other contexts.
    # However, in JSON color lists, it's usually a direct string value.
    if original_text.lower() == '"transparent"':
        return original_text
    return f'"{random_hex_color()}"'

  modified_content = re.sub(hex_color_regex, replacer, content)

  try:
    json.loads(modified_content) # Validate JSON
  except json.JSONDecodeError as e:
    print(f"Error: Modified content for {filepath} is not valid JSON. {e}")
    # Optionally, write the problematic content to a temp file for inspection
    # with open(f"error_json_{filepath}.json", "w") as err_f:
    #    err_f.write(modified_content)
    return False # Indicate failure

  try:
    with open(filepath, 'w') as f:
      f.write(modified_content)
    print(f"Successfully updated colors in {filepath}")
    return True # Indicate success
  except IOError as e:
    print(f"Error writing to file {filepath}: {e}")
    return False # Indicate failure

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Replace hex color codes in a JSON file with random ones.")
  parser.add_argument("filepath", help="The path to the JSON file to process.")
  args = parser.parse_args()

  if not args.filepath.endswith(".json"):
    print("Error: Please provide a .json file.")
  elif not replace_colors_in_file(args.filepath):
    # If the function returned False, exit with an error code
    exit(1)
