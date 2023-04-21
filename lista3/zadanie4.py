import qrcode
import cv2

# Wygenerowanie kodu QR
data = "https://pbs.twimg.com/media/EXRTYNbXkAA6nRa.png"
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img_qr = qr.make_image(fill_color='black', back_color='white')
img_qr.save("qr_code.png")

# Odczytanie kodu QR
img = cv2.imread("qr_code.png")
detector = cv2.QRCodeDetector()
data, points, straight_qrcode = detector.detectAndDecode(img)

if data:
    print("Odczytany kod QR to:", data)
else:
    print("Nie udało się odczytać kodu QR.")
