import base64

def encode_file(file):
    try:
        file_content = file.read()
        encoded_content = base64.b64encode(file_content)
        return encoded_content
    except Exception as e:
        raise ValueError(f"Error encoding file: {str(e)}")

def decode_file(file_content):
    try:
        decoded_content = base64.b64decode(file_content)
        return decoded_content
    except Exception as e:
        raise ValueError(f"Error decoding file: {str(e)}")

def utf8_to_base64(utf8_text):
    utf8_bytes = utf8_text.encode('utf-8')
    base64_bytes = base64.b64encode(utf8_bytes)
    return base64_bytes.decode('utf-8')

def base64_to_utf8(base64_text):
    base64_bytes = base64_text.encode('utf-8')
    utf8_bytes = base64.b64decode(base64_bytes)
    return utf8_bytes.decode('utf-8')
