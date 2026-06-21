import qrcode
import os

data = input("Enter the text or URL: ").strip()
filename = input("Enter filename: ").strip()

if not filename.endswith(".png"):
    filename += ".png"

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)

full_path = os.path.abspath(filename)

print("QR code saved at:")
print(full_path)

# Open image
os.startfile(full_path)