import qrcode
from PIL import Image
import qrcode.constants

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,
                 border=4,)

#enter the link to generate qr
qr.add_data("https://www.youtube.com/")
qr.make(fit=True)

#your desired color scheme
img=qr.make_image(fill_color="yellow",back_color="blue")
img.save("outputqr.png")
