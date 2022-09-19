from asyncio import constants
from turtle import fillcolor
import qrcode


def gen_QR_code(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img =qr.make_image(fillcolor ="black", backcolor = "white")
    img.save("little_projects\QRcodeGen\QR.png")

text = input("Text to QR:  ")
gen_QR_code(str(text))