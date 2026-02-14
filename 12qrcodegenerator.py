import qrcode
input_URL = "https://www.linkedin.com/in/nisha-nisha-b01854343?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"
qr = qrcode.QRCode(
    version = 1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border = 4,
)
qr.add_data(input_URL)
qr.make(fit=True)
img=qr.make_image(fill_color="red",black_color="white")
img.save("url_qrcode.png")
print(qr.data_list)