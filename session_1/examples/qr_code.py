import qrcode

img = qrcode.make("Welcome everybody to Mintic 2022!!")
img.save("minticQR.jpg")
