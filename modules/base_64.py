import base64
import multiprocessing

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
        return b''.join(encoded_chunks)
    except Exception as e:
        raise ValueError(f"Error encoding file: {str(e)}")

def decode_file(file_content):
    try:
        pool = multiprocessing.Pool()
        decoded_chunks = pool.map(decode_chunk, iter(lambda: file_content.read(65536), b''))
        pool.close()
        pool.join()
        return b''.join(decoded_chunks)
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
