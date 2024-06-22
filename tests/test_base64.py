import base64
import io
import pytest
from modules.base_64 import encode_file, decode_file, utf8_to_base64, base64_to_utf8

def test_encode_file():
    file = io.BytesIO(b"test content")
    encoded = encode_file(file)
    assert encoded == base64.b64encode(b"test content")

def test_encode_file_error():
    with pytest.raises(ValueError, match="Error encoding file"):
        encode_file(None)

def test_decode_file():
    encoded_content = base64.b64encode(b"test content")
    decoded = decode_file(encoded_content)
    assert decoded == b"test content"

def test_decode_file_error():
    with pytest.raises(ValueError, match="Error decoding file"):
        decode_file(b"not base64")

def test_utf8_to_base64():
    utf8_text = "hello world"
    base64_text = utf8_to_base64(utf8_text)
    assert base64_text == base64.b64encode(utf8_text.encode('utf-8')).decode('utf-8')

def test_base64_to_utf8():
    base64_text = base64.b64encode(b"hello world").decode('utf-8')
    utf8_text = base64_to_utf8(base64_text)
    assert utf8_text == "hello world"
