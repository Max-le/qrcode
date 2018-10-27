

# Documentation : https://pypi.org/project/qrcode/

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=1,
    border=4,
)
qr.add_data('HELLO WORLD !!! ')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="transparent")
img.show()