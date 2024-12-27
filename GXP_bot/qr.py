import qrcode

def create_giphy_qr():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Direct link to the Giphy animation
    giphy_url = "https://giphy.com/gifs/26tOZ42Mg6pbTUPHW"

    qr.add_data(giphy_url)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save("newyear_giphy_qr.png")
    print("Created QR code: newyear_giphy_qr.png")
    print("When scanned, this will open the Giphy animation!")

create_giphy_qr()
