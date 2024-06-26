from modules.QR_generator import generate_qr_code
import base64

def test_generate_qr_code():
    data = "https://example.com"
    qr_code_base64 = generate_qr_code(data)
    assert qr_code_base64.startswith("iVBORw0KGgoAAAANSUhEUg")

    img_bytes = base64.b64decode(qr_code_base64)
    assert img_bytes.startswith(b'\x89PNG\r\n\x1a\n')
