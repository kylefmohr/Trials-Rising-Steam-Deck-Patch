import sys
import getpass

# Check if user specified a path
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = '/home/' + getpass.getuser() + '/.local/share/Steam/steamapps/common/Trials Rising/datapack/trialsrising.exe'

# Some explanation: these bytes first serve as hex representations of the program instructions we want to change
# But if that was all they needed to be, they could each be 3 hex characters long:
# original_bytes = b'\x48\x89\x54'
# new_and_improved_bytes = b'\xB0\x01\xC3'
# However the issue is that this sequence of original_bytes shows up many many times in the executable, 
# so we would end up patching many places that don't need to be patched, 
# causing unintended functionality (likely) or else just causing the program to crash (extremely likely)
# instead, we specify *just* enough bytes such that the sequence only occurs in one place:
original_bytes = b'\x48\x89\x54\x24\x10\x55\x56\x57\x48\x81\xEC\xF0\x00\x00\x00\x48\xC7\x44\x24\x78'
# translated (from Ghidra (used to disassemble this program)):                                                                                  15a0b00dc(*)  
#        14178b6c0 48 89 54        MOV        qword ptr [RSP + 0x10],RDX
#                  24 10
#        14178b6c5 55              PUSH       RBP
#        14178b6c6 56              PUSH       RSI
#        14178b6c7 57              PUSH       RDI
#        14178b6c8 48 81 ec        SUB        RSP,0xf0
#                  f0 00 00 00
#        14178b6cf 48 c7 44        MOV        qword ptr [RSP + 0x78],-0x2
#                  24 78 fe 
#                  ff ff ff
new_and_improved_bytes = b'\xB0\x01\xC3\x24\x10\x55\x56\x57\x48\x81\xEC\xF0\x00\x00\x00\x48\xC7\x44\x24\x78'
# Translated:
# mov al, 1
# ret
# (then the rest of these bytes don't matter because they will never be reached)
# or in pseudocode, `return True;`


try:
    with open(path, 'rb') as file:
        # read the .exe file
        data = file.read()
except FileNotFoundError:
    print(f"Error: The file '{path}' was not found.")
    print("Hint: specify the path to the .exe as a command line argument, like this:")
    print(f"python {sys.argv[0]} /path/to/trialsrising.exe")
    sys.exit(1)

# Perform the replacement, limited to 1 occurrence
patched_data = data.replace(original_bytes, new_and_improved_bytes, 1)

# Ensure we actually changed *something*
if patched_data != data:
    # Write the modified data back to the file
    with open(path, 'wb') as file:
        file.write(patched_data)
    print(f"Success: Byte sequence found and replaced in {path}.")
else:
    print("Notice: The search sequence was not found in the binary, no changes were made.")

