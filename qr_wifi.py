

# Documentation : https://pypi.org/project/qrcode/

import qrcode
from PIL import ImageOps
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=25,
    border=4,
)

#Sensitive info 
qr.add_data('WIFI:T:WPA;S:Eskimo;P:24mar10iel62fr;;')

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="transparent")
img.show()
img.save('wifi.png')
