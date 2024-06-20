import base64
import multiprocessing

BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def utf8_to_base64(utf8_text):
    utf8_bytes = utf8_text.encode('utf-8')
    base64_bytes = base64.b64encode(utf8_bytes)
    return base64_bytes.decode('utf-8')

def base64_to_utf8(base64_text):
    base64_bytes = base64_text.encode('utf-8')
    utf8_bytes = base64.b64decode(base64_bytes)
    return utf8_bytes.decode('utf-8')

def encode_chunk(chunk):
    return base64.b64encode(chunk)

def decode_chunk(chunk):
    return base64.b64decode(chunk)

def encode_file(file):
    try:

        pool = multiprocessing.Pool()
        encoded_chunks = pool.map(encode_chunk, iter(lambda: file.read(65536), b''))

        pool.close()
        pool.join()

        b64_encoded_parts = b''.join(encoded_chunks)

        return b64_encoded_parts
    except Exception as e:
        raise ValueError(f"Error encoding file: {str(e)}")

def decode_file(base64_content, original_filename):
    try:

        pool = multiprocessing.Pool()

        chunk_size = 65536
        base64_chunks = [base64_content[i:i + chunk_size] for i in range(0, len(base64_content), chunk_size)]
        decoded_chunks = pool.map(decode_chunk, base64_chunks)

        pool.close()
        pool.join()

        decoded_parts = b''.join(decoded_chunks)

        return decoded_parts
    except Exception as e:
        raise ValueError(f"Error decoding Base64: {str(e)}")
