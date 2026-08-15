import qrcode
import os

livres = {
    1: "https://automatetheboringstuff.com/",
    2: "https://www.khanacademy.org/math",
    3: "https://www.khanacademy.org/science/physics",
    4: "https://www.allaboutcircuits.com/textbook/",
}

os.makedirs("static", exist_ok=True)

for id_livre, url in livres.items():
    img = qrcode.make(url)
    img.save(f"static/qr_livre_{id_livre}.png")
    print(f"QR code créé pour le livre {id_livre} → {url}")

print("Terminé !")
