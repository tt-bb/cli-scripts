import os

import qrcode

# Generate QRCode
qr = qrcode.QRCode()
data = input("Enter the data of the QRCode > ")
qr.add_data(data)
qr.make()
fill = input("Enter the color of the grid (#HEX) > ")
back = input("Enter the color of the background (#HEX) > ")
img = qr.make_image(fill_color=fill, back_color=back)

# Save the QRCode in the folder qrcode/ from CWD
qr_code_path = (
    os.path.dirname(os.path.realpath(__file__))
    + os.sep
    + "qrcode"
    + os.sep
    + "qrcode.png"
)
img.save(qr_code_path)
