import os
import shutil
import getpass

def modify_exe(input_path):
    steam_version_offset = 0x0178ACC0
    ubisoft_connect_version_offset = 0x01789EE0
    expected_bytes = bytes.fromhex("48 89 54 24 10 55 56 57 48 81 EC F0 00 00 00 48")
    replacement_bytes = bytes.fromhex("B0 01 C3 24 10 55 56 57 48 81 EC F0 00 00 00 48")
    expected_path_linux = '/home/' + getpass.getuser() + '/.local/share/Steam/steamapps/common/Trials Rising/datapack/trialsrising.exe'

    if not os.path.exists(input_path):
        if os.path.exists(expected_path_linux):
            input_path = expected_path_linux
        else:
            print("Error: Could not find trialsrising.exe")
            return False

    try:
        with open(input_path, 'rb') as infile:
            data = bytearray(infile.read())

            def check_and_patch(offset):
                if offset + len(expected_bytes) > len(data):
                    return False, "Offset exceeds file size"
                read_bytes = bytes(data[offset: offset + len(expected_bytes)])
                if read_bytes == expected_bytes:
                    print(f"Bytes matched at offset: {hex(offset)}. Modifying...")
                    for i, byte in enumerate(replacement_bytes):
                        data[offset + i] = byte
                    return True, None
                return False, "Bytes did not match"

            modified, message = check_and_patch(steam_version_offset)

            if not modified:
                print("This does not appear to be a Steam version of the game. Checking if it's Ubisoft Connect version...")
                modified, message = check_and_patch(ubisoft_connect_version_offset)
                if not modified:
                    print("Error: could not find bytes to patch. Is it possible that the file is already patched?")
                    print("Ensure you're only trying to patch the original trialsrising.exe file.")
                    return False

            if modified:
                # backup original file
                backup_path = os.path.splitext(input_path)[0] + "_original.exe"
                shutil.copy(input_path, backup_path)
                print(f"Backed up original file to: {backup_path}")
                # write patched exe
                with open(input_path, 'wb') as outfile:
                    outfile.write(data)
                print(f"Successfully patched file: {input_path}")
                return True
            return False


    except FileNotFoundError:
        print(f"Error: Input file not found: {input_path}")
        return False
    except IOError as e:
        print(f"Error: IO error occurred: {e}")
        return False


if __name__ == '__main__':
    # Replace 'test.exe' with the actual path of your .exe file for testing
    input_file = input("Enter the path of the trialsrising.exe file, or press Enter to use the default path: ")
    if modify_exe(input_file):
        print("Process completed.")
    else:
        print("Process failed.")
