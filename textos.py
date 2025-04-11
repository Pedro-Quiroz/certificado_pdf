from reportlab.lib.colors import HexColor
import qrcode

def contenido_texto_inicio(c, ancho_pagina):
    c.setFont("OpenSans_regular", 19.6)
    c.setFillColor(HexColor("#180770"))
    c.drawCentredString((ancho_pagina/2), 479, "Certifica a")
    c.drawCentredString((ancho_pagina/2), 427, "Por participar y aprobar el")

def contenido_titulo(c, ancho_pagina):
    c.setFont("OpenSans_regular", 23.4)
    c.setFillColor(HexColor("#180770"))
    c.drawCentredString((ancho_pagina/2)+3, 374, "CURSO")

def contenido_estudiante(c,estudiante,ancho_pagina):
    # Agrega contenido al PDF
    c.setFont("OpenSans_negrita", 27)
    c.setFillColor(HexColor("#180770"))
    c.drawCentredString((ancho_pagina/2)+3, 449, estudiante)
    
def contenido_curso(c,curso,ancho_pagina):
    # Agrega contenido al PDF
    c.setFont("OpenSans_negrita", 30.8)
    c.setFillColor(HexColor("#180770"))
    lineas = curso.split()
    nueva_linea = ""
    for palabra in lineas:
        nueva_linea = nueva_linea + " " + palabra
        ancho_actual = c.stringWidth(nueva_linea, "OpenSans_negrita", 30.8)
        if ancho_actual > 700:
            c.drawCentredString(ancho_pagina/2, 339.5, nueva_linea)
            nueva_linea = ""
    c.drawCentredString(ancho_pagina/2,297, nueva_linea)    

def contenido_texto_fin(c,horas,ancho_pagina):
    # Agrega contenido al PDF
    c.setFont("OpenSans_regular", 9.3)
    c.setFillColor(HexColor("#180770"))
    c.drawCentredString(ancho_pagina/2+3, 88, "Certificado de aprobación:")
    c.drawCentredString(ancho_pagina/2+1, 54, f"{horas} horas de práctica")

def contenido_fecha(c,fecha,ancho_pagina):
    # Agrega contenido al PDF
    c.setFont("OpenSans_negrita", 12)
    c.setFillColor(HexColor("#180770"))
    c.drawCentredString(ancho_pagina/2, 70, fecha)

def contenido_link(c,link,ancho_pagina):
    # Agrega contenido al PDF
    c.setFont("OpenSans_negrita", 8.9)
    c.setFillColor(HexColor("#180770"))
    c.drawCentredString(ancho_pagina/2+1, 38.5, link)

def generar_qr(c,link):
    # Crea un objeto QRCode
    qr = qrcode.QRCode(version=1, box_size=3, border=0)
    qr.add_data(link)
    # Compila el objeto QRCode en una imagen
    qr.make(fit=True)
    # Guarda la imagen en un archivo
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("codigo_qr.png")
    c.drawImage("codigo_qr.png",720,477)
