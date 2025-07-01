import os
import shutil
import getpass

def modify_exe(input_path):
    steam_version_offset = 0x0178bac2
    #ubisoft_connect_version_offset = 0x01789EE0
    expected_bytes = bytes.fromhex("40 0f b6 c7 0f 28 74 24 50 48 83 c4 68 5f 5b c3")
    replacement_bytes = bytes.fromhex("31 C0 B0 01 0f 28 74 24 50 48 83 c4 68 5f 5b c3")
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
                # Search for the expected bytes throughout the entire file, not just at the offset
                # for i in range(len(data) - len(expected_bytes)):
                #     read_bytes = bytes(data[i: i + len(expected_bytes)])
                #     if read_bytes == expected_bytes:
                #         print(f"Found expected bytes at offset: {hex(i)}")
                #         offset = i
                #         continue
                # exit()
                if read_bytes == expected_bytes:
                    print(f"Bytes matched at offset: {hex(offset)}. Modifying...")
                    for i, byte in enumerate(replacement_bytes):
                        data[offset + i] = byte
                    return True, None
                elif read_bytes == replacement_bytes:
                    print(f"Bytes already modified at offset: {hex(offset)}, no changes made.")
                    return False, "Program already patched"
                else:
                    print(f"These bytes: {read_bytes.hex()} did not match expected bytes: {expected_bytes.hex()}")
                return False, "Bytes did not match"

            modified, message = check_and_patch(steam_version_offset)

            if not modified:
                print(f"Error: {message}")
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
    input_file = input("Enter the path of the trialsrising.exe file, or press Enter to use the default path: ")
    if modify_exe(input_file):
        print("Process completed.")
    else:
        print("Process failed.")
