"""Gera as fotos do site (cf-site) a partir dos originais desta pasta.

Rodar de novo sempre que trocar ou incluir foto:  python preparar-fotos.py
Os originais nunca são alterados; o cf-site é sobrescrito.
"""
import os
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(AQUI, "cf-site")

# página inicial: mesmo nome do original, lado maior 1600 px
INICIO = [
    "hope-00-perfil.jpg", "hope-post-01.jpg", "hope-post-02.jpg", "hope-post-06.jpg",
    "hope-post-07.jpg", "hope-post-08.jpg", "hope-post-09.jpg", "hope-post-10.jpg",
]

# catálogo: (arquivo de saída, original, recorte em pixels ou None)
# os recortes dos destaques (320x569) tiram a legenda do story
CATALOGO = [
    ("cat-difusor-flor-caramelo.jpg", "hope-post-09.jpg", None),
    ("cat-difusor-flores-canelado.jpg", "hope-post-06.jpg", None),
    ("cat-difusor-flores-no-frasco.jpg", "hope-post-02.jpg", None),
    ("cat-difusor-flor-azul.jpg", "hope-destaque-produtos-02.jpg", (0, 160, 320, 560)),
    ("cat-vela-flor.jpg", "hope-post-10.jpg", None),
    ("cat-vela-luminaria.jpg", "hope-post-04.jpg", None),
    ("cat-vela-pote-de-vidro.jpg", "hope-destaque-grupo-vip-01.jpg", (0, 335, 320, 569)),
    ("cat-velas-lembrancinha.jpg", "hope-destaque-produtos-04.jpg", (0, 120, 320, 520)),
    ("cat-kit-lavabo.jpg", "hope-destaque-produtos-01.jpg", (0, 169, 320, 569)),
    ("cat-kit-perfume-sabonete.jpg", "hope-post-07.jpg", None),
    ("cat-kit-difusor-sabonete.jpg", "hope-post-11.jpg", None),
]


def salvar(origem, destino, lado, recorte=None):
    im = Image.open(os.path.join(AQUI, origem)).convert("RGB")
    if recorte:
        im = im.crop(recorte)
    im.thumbnail((lado, lado), Image.LANCZOS)
    im.save(os.path.join(SITE, destino), "JPEG", quality=80, optimize=True, progressive=True)


for f in INICIO:
    salvar(f, f, 1600)
for destino, origem, recorte in CATALOGO:
    salvar(origem, destino, 1000, recorte)

total = sum(os.path.getsize(os.path.join(SITE, f)) for f in os.listdir(SITE))
print(f"ok — {len(INICIO) + len(CATALOGO)} fotos, cf-site com {total // 1024} KB")
