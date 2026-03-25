"""
GENERADOR DE QR – I.E. 0027 "San Antonio de Jicamarca"
Ejecuta: py 1_generar_qr.py
"""

import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

ALUMNOS = [
    "Aguilera De La Cruz, Leonel Dylan",
    "Aponte Huancaya, Rafael Aaron",
    "Ayala Morales, Diego James",
    "Balbin Bautista, Sully Cielo Alejandra",
    "Bellido Meneses, Jamilett Maria",
    "Cabrera Osorio, Liam Fabricio",
    "Campos Torres, Brianna Kasumi",
    "Canahualpa Masquez, Luna Mafer",
    "Diaz Briceño, Pedro Keylor",
    "Espinoza Reymundo, Juan Cesar",
    "Gonzales Huerta, Jhon Kelvin",
    "Huaman Oscco, Kenia Elif",
    "Huaroc Palomino, Anjalí Tiana",
    "Huaynates Durand, Jose Alexis",
    "Jara Pineda, Ashley Luz",
    "Laureano Surichaqui, Mael Raul",
    "Medina Huisa, Galet Jacob",
    "Natividad Bardales, Brayden Emilio",
    "Ortega Taipe, Jordan Ibraimovic",
    "Palomino Limas, Liam Manuel",
    "Quispe Porras, Yahiko Deyvis",
    "Rodriguez Berrospi, Jhunior Steven",
    "Rojas De La Cruz, Alessia Luciana",
    "Sánchez Cajacuri, Adeline Taylor",
    "Silva Bernardo, Yefrey Delson",
    "Soto Yañac, Sebastián",
    "Tito Gozme, Adrian Gael",
    "Valdivia Sumaran, Gael Jesús",
    "Vallejo Salazar, Iker Gael",
    "Vargas Mendoza, Yeico Jandel",
    "Vasquez Medrano, Piero",
    "Zuca Curi, Cielo",
]

INSTITUCION = 'I.E. 0027 "San Antonio"'
SALON       = "3 F"
OUTPUT_DIR  = "qr_alumnos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

CARD_W  = 420
CARD_H  = 540
QR_SIZE = 300

def make_card(nombre, alumno_id, numero):
    card = Image.new("RGB", (CARD_W, CARD_H), "white")
    draw = ImageDraw.Draw(card)

    # ── Encabezado azul ───────────────────────────────────────────────────────
    draw.rectangle([0, 0, CARD_W, 60], fill="#1a237e")
    draw.text((CARD_W // 2, 16), INSTITUCION,
              fill="white", anchor="mm", font=ImageFont.load_default())
    draw.text((CARD_W // 2, 34), f"Salón: {SALON}",
              fill="#90caf9", anchor="mm", font=ImageFont.load_default())
    draw.text((CARD_W // 2, 50), f"N° {numero}  |  {alumno_id}",
              fill="#bbdefb", anchor="mm", font=ImageFont.load_default())

    # ── Código QR ─────────────────────────────────────────────────────────────
    qr_data = f"ASIST|{alumno_id}|{nombre}"
    qr = qrcode.QRCode(
        version=2, box_size=8, border=2,
        error_correction=qrcode.constants.ERROR_CORRECT_M
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="#1a237e", back_color="white").convert("RGB")
    qr_img = qr_img.resize((QR_SIZE, QR_SIZE), Image.LANCZOS)
    card.paste(qr_img, ((CARD_W - QR_SIZE) // 2, 70))

    # ── ID debajo del QR ──────────────────────────────────────────────────────
    draw.rectangle([30, 378, CARD_W - 30, 396], fill="#e8eaf6")
    draw.text((CARD_W // 2, 387), alumno_id,
              fill="#1a237e", anchor="mm", font=ImageFont.load_default())

    # ── Nombre en fondo azul ──────────────────────────────────────────────────
    draw.rectangle([0, 408, CARD_W, 490], fill="#1a237e")

    # Dividir nombre en líneas si es largo
    palabras = nombre.split()
    if len(palabras) <= 3:
        draw.text((CARD_W // 2, 449), nombre,
                  fill="white", anchor="mm", font=ImageFont.load_default())
    elif len(palabras) == 4:
        l1 = " ".join(palabras[:2])
        l2 = " ".join(palabras[2:])
        draw.text((CARD_W // 2, 430), l1,
                  fill="white", anchor="mm", font=ImageFont.load_default())
        draw.text((CARD_W // 2, 452), l2,
                  fill="white", anchor="mm", font=ImageFont.load_default())
    else:
        l1 = " ".join(palabras[:3])
        l2 = " ".join(palabras[3:])
        draw.text((CARD_W // 2, 425), l1,
                  fill="white", anchor="mm", font=ImageFont.load_default())
        draw.text((CARD_W // 2, 445), l2,
                  fill="white", anchor="mm", font=ImageFont.load_default())

    # ── Pie ───────────────────────────────────────────────────────────────────
    draw.text((CARD_W // 2, 515), "Escanear para registrar asistencia",
              fill="#9e9e9e", anchor="mm", font=ImageFont.load_default())

    # ── Borde ─────────────────────────────────────────────────────────────────
    draw.rectangle([0, 0, CARD_W - 1, CARD_H - 1],
                   outline="#1a237e", width=3)
    return card


print("=" * 55)
print('  GENERADOR DE QR – I.E. 0027 "San Antonio de Jicamarca"')
print("=" * 55)
print()

for i, nombre in enumerate(ALUMNOS, start=1):
    # ID sin caracteres especiales para el nombre de archivo
    safe = nombre.replace(",", "").replace(" ", "_")
    safe = safe.encode("ascii", "ignore").decode()
    alumno_id = f"ALU{i:03d}"
    card      = make_card(nombre, alumno_id, i)
    filename  = f"{OUTPUT_DIR}/{i:02d}_{alumno_id}_{safe[:30]}.png"
    card.save(filename)
    print(f"  ✓  {i:02d}.  {alumno_id}  {nombre}")

print()
print(f"✅ {len(ALUMNOS)} tarjetas guardadas en '{OUTPUT_DIR}/'")
print()
print("Abre la carpeta 'qr_alumnos' e imprime las tarjetas.")