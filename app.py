from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from textos import  *
# Registra la fuente personalizada en ReportLab
pdfmetrics.registerFont(TTFont("OpenSans_negrita", "OpenSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("OpenSans_regular", "OpenSans-Regular.ttf"))

background_image_path = "Camioneta_fondo.png"
nombre_estudiante = "PEDRO FERNANDO QUIROZ ANDAMAYO"
nombre_curso = "TÉCNICA DE CONDUCCIÓN DE CAMIONETA TOYOTA HILUX 4x4"
fecha = "Aprobado el 04 de Octubre del 2024"
horas = 8
# LINK
nombre_formateado = nombre_estudiante.lower().replace(" ", "-")
link = f"https://www.paginaweb.com/{nombre_formateado}"
file_name = f"{nombre_estudiante}.pdf"
def create_pdf(file_name, background_image_path):
    c = canvas.Canvas(file_name, pagesize=landscape(A4))
    page_width, page_height = (A4[1], A4[0])
    c.drawImage(background_image_path, 0, 0, width=page_width, height=page_height, preserveAspectRatio=True)
    contenido_texto_inicio(c, page_width)
    contenido_titulo(c, page_width)
    contenido_estudiante(c,nombre_estudiante,page_width)
    contenido_curso(c,nombre_curso,page_width)
    contenido_texto_fin(c,horas,page_width)
    contenido_fecha(c,fecha,page_width)
    contenido_link(c,link,page_width)
    generar_qr(c,link)
    c.save()


create_pdf(file_name, background_image_path)