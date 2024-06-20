import qrcode
import io
import base64
from PIL import Image


def generate_qr_code(data, fill_color='black', back_color='white'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')

    img_byte_arr = io.BytesIO()
    qr_img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    img_base64 = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')

    return img_base64
