import qrcode
from pathlib import Path

def create_qr_code(data: str, filename: str = "qrcode.png", color: str = "black") -> Path:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color, back_color="white")
    output_path = Path(filename)
    if output_path.suffix.lower() != '.png':
        output_path = output_path.with_suffix('.png')
    img.save(output_path)
    return output_path
