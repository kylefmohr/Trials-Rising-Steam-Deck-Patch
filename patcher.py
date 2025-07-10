import bsdiff4
import zlib
import getpass
import shutil
from sys import exit

def verify_checksum(file_path, expected_checksum):
    """
    Verify the checksum of a file against an expected checksum.
    
    :param file_path: Path to the file to verify.
    :param expected_checksum: Expected checksum value.
    :return: True if the checksum matches, False otherwise.
    """
    try:
        actual_checksum = zlib.crc32(open(file_path, 'rb').read())
        print(f"Expected checksum: {expected_checksum}, Actual checksum: {actual_checksum}")
        return actual_checksum == expected_checksum
    except Exception as e:
        print(f"Error verifying checksum: {e}")
        return False

def apply_patch(old_file_path, new_file_path, patch_bytes):
    """
    Apply a binary patch to an old file to create a new file.
    
    :param old_file_path: Path to the old file.
    :param new_file_path: Path where the new file will be saved.
    :param patch_bytes: The binary patch data.
    """
    try:
        with open(old_file_path, 'rb') as old_file:
            old_data = old_file.read()
        
        new_data = bsdiff4.patch(old_data, patch_bytes)
        
        with open(new_file_path, 'wb') as new_file:
            new_file.write(new_data)
        
        print(f"Patch applied successfully. New file created at {new_file_path}")
    except Exception as e:
        print(f"Error applying patch: {e}")

patch_bytes = b"\x42\x53\x44\x49\x46\x46\x34\x30\x3E\x00\x00\x00\x00\x00\x00\x00\x2E\x01\x00\x00\x00\x00\x00\x00\xA8\x0C\x6E\x14\x00\x00\x00\x00\x42\x5A\x68\x39\x31\x41\x59\x26\x53\x59\xED\xED\xC0\x27\x00\x00\x07\x63\x51\xC0\x44\x14\x00\x20\x00\x00\x01\x40\x00\x00\x40\x10\x00\x02\x00\x20\x00\x31\x00\xD3\x4D\x04\x34\x06\x9A\x50\xA0\xEC\x51\x46\xD7\x2F\x17\x72\x45\x38\x50\x90\xED\xED\xC0\x27\x42\x5A\x68\x39\x31\x41\x59\x26\x53\x59\xD5\x2F\x49\xC5\x00\xBD\x1A\xC9\x89\xC0\x20\x00\x10\x00\x40\x80\x40\x20\x00\x10\x00\x20\x18\x20\x00\x50\x80\x69\xA6\x81\x35\x54\x1A\x1B\x53\x28\xD7\x08\x08\x12\xEF\xA9\x49\x20\xAA\xB3\x7F\x7D\x9A\xDE\x72\xA2\xA0\x25\xF9\x8A\x0A\xC9\x32\x9A\xC8\x70\x4F\x16\xF8\x0A\xFC\x72\x00\x06\x00\x00\x00\x41\x00\x01\x84\x02\x6A\x32\x15\x01\x2D\x48\x54\x04\xB9\x8A\x0A\xC9\x32\x9A\xC8\x70\x4F\x16\xF8\x0A\xFC\x72\x00\x06\x00\x00\x00\x41\x00\x01\x84\x02\x6A\x32\x15\x01\x2D\x48\x54\x04\xB9\x8A\x0A\xC9\x32\x9A\xC8\x70\x4F\x16\xF8\x0A\xFC\x72\x00\x06\x00\x00\x00\x41\x00\x01\x84\x02\x6A\x32\x15\x01\x2D\x48\x54\x04\xB9\x8A\x0A\xC9\x32\x9A\xC8\x70\x4F\x16\xF8\x0A\xFC\x72\x00\x06\x00\x00\x00\x41\x00\x01\x84\x02\x6A\x32\x15\x01\x2D\x48\x54\x04\xB9\x8A\x0A\xC9\x32\x9A\xC8\x70\x4F\x16\xF8\x0A\xFC\x72\x00\x06\x00\x00\x00\x41\x00\x01\x84\x02\x6A\x32\x15\x01\x2D\x48\x54\x04\xB9\x8A\x0A\xC9\x32\x9A\xC8\x70\x4F\x16\xF8\x0A\xFC\x72\x00\x06\x00\x00\x00\x41\x00\x01\x84\x02\x6A\x32\x15\x01\x2D\x48\x54\x04\xB9\x8A\x0A\xC9\x32\x9A\xCB\xF2\xD1\x6B\xA0\x05\x23\x1E\x40\x06\x00\x00\x02\x00\x00\x41\x00\x01\x86\x60\x29\x4D\x35\x42\x84\x4D\x81\x14\x22\x78\xBB\x92\x29\xC2\x84\x80\xF2\xFA\xB3\xB0\x42\x5A\x68\x39\x17\x72\x45\x38\x50\x90\x00\x00\x00\x00"
expected_path = '/home/' + getpass.getuser() + '/.local/share/Steam/steamapps/common/Trials Rising/datapack/trialsrising.exe'
new_path = expected_path + '.new'
expected_checksum_before = 0xF197E04E
expected_checksum_after = 0x883925BD

if verify_checksum(expected_path, expected_checksum_before):
    apply_patch(expected_path, new_path, patch_bytes)

    if verify_checksum(new_path, expected_checksum_after):
        print("Patch applied successfully.")
    else:
        print("Patch failed: checksum mismatch after patching. Please open an issue on GitHub.")
        exit(1)
    
    try:
        shutil.move(new_path, expected_path)
    except Exception as e:
        print(f"Error replacing old file with new file: {e}")
        exit(1)
else:
    if(verify_checksum(expected_path, expected_checksum_after)):
        print("Patch has already been applied, no changes made.")
        exit(0)
    print("Patch failed: checksum mismatch before patching. Go to the game's properties in Steam > Installed Files > Verify integrity of game files, then try again")
    print("If that doesn't work, please open an issue on GitHub.")
    exit(1)

