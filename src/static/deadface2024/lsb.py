def binary_to_ascii(binary_string):
    ascii_characters = []
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i + 8]
        if len(byte) == 8:
            ascii_characters.append(chr(int(byte, 2)))
    return ''.join(ascii_characters)

def binary_to_utf8(binary_string):
    utf8_bytes = bytearray()
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i + 8]
        if len(byte) == 8:
            utf8_bytes.append(int(byte, 2))
    return utf8_bytes.decode('utf-8', errors='ignore')

def extract_lsb(file_path):
    # Open file
    with open(file_path, 'rb') as file:
        data = file.read()

    # Extract LSB
    byte_data = bytearray(data)
    lsb_result = ''.join(str(byte & 1) for byte in byte_data)

    # Convert LSB result to ASCII
    ascii_result = binary_to_ascii(lsb_result)
    with open('ascii.txt', 'w', encoding='utf-8') as ascii_file:
        ascii_file.write(ascii_result)
    print("ASCII Conversion saved to ascii.txt")

    # Convert LSB result to UTF-8
    utf8_result = binary_to_utf8(lsb_result)
    with open('utf.txt', 'w', encoding='utf-8') as utf8_file:
        utf8_file.write(utf8_result)
    print("UTF-8 Conversion saved to utf.txt")

# Example usage
file_path = 'electricsoldiers.mp3'
extract_lsb(file_path)
