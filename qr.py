

# Documentation : https://pypi.org/project/qrcode/

import qrcode
from PIL import ImageOps
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data('http://qonnect.ml')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="transparent")
img.show()
img.save('test.png')
img = ImageOps.invert(img)
img.show()
