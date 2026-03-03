import sys
import getpass

# Check if user specified a path
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = '/home/' + getpass.getuser() + '/.local/share/Steam/steamapps/common/Trials Rising/datapack/trialsrising.exe'

original_bytes = b'\x48\x89\x54\x24\x10\x55\x56\x57\x48\x81\xEC\xF0\x00\x00\x00\x48\xC7\x44\x24\x78'
new_and_improved_bytes = b'\xB0\x01\xC3\x24\x10\x55\x56\x57\x48\x81\xEC\xF0\x00\x00\x00\x48\xC7\x44\x24\x78'

try:
    with open(path, 'rb') as file:
        data = file.read()
except FileNotFoundError:
    print(f"Error: The file '{path}' was not found.")
    sys.exit(1)

# Perform the replacement, limited to 1 occurrence
patched_data = data.replace(original_bytes, new_and_improved_bytes, 1)

# Check if anything was actually changed
if patched_data != data:
    # Write the modified data back to the file
    with open(path, 'wb') as file:
        file.write(patched_data)
    print(f"Success: Byte sequence found and replaced in {path}.")
else:
    print("Notice: The search sequence was not found in the binary, no changes were made.")

