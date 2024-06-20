import base64

BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def utf8_to_base64(utf8_text):
    utf8_bytes = utf8_text.encode('utf-8')
    base64_bytes = base64.b64encode(utf8_bytes)
    return base64_bytes.decode('utf-8')

def base64_to_utf8(base64_text):
    base64_bytes = base64_text.encode('utf-8')
    utf8_bytes = base64.b64decode(base64_bytes)
    return utf8_bytes.decode('utf-8')

def encode_file(file_content):
    base64_bytes = base64.b64encode(file_content)
    return base64_bytes.decode('utf-8')

def decode_file(base64_content):
    try:
        file_content = base64.b64decode(base64_content)
        return file_content
    except Exception as e:
        raise ValueError(f"Error decoding Base64: {str(e)}")
