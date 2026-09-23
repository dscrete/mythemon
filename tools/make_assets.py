#!/usr/bin/env python3
"""Generate original four-shade static assets for Aeglet.

Dimensions follow Gen1Recomp's compact custom-species example:
40x40 front (frontSize 5), 32x32 back, and a 16x32 two-frame icon.

Assets are written as plain grayscale PNGs rather than indexed-palette PNGs.
This keeps the files simple for LÖVE and makes CRC validation straightforward.
"""
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent / "assets"
SHADES = [(248,248,248),(168,168,168),(88,88,88),(8,8,8)]


def canvas(size):
    im = Image.new("P", size, 0)
    pal = [v for rgb in SHADES for v in rgb] + [0] * (768 - 12)
    im.putpalette(pal)
    return im


def front():
    im = canvas((40,40)); d = ImageDraw.Draw(im)
    d.line([(28,29),(33,27),(36,23),(36,18),(33,14),(30,13)], fill=3, width=5)
    d.line([(29,28),(32,26),(34,22),(34,18),(32,16),(30,15)], fill=1, width=2)
    d.ellipse((13,19,31,32), fill=3)
    d.ellipse((15,20,29,30), fill=1)
    d.polygon([(14,27),(20,27),(19,37),(14,37)], fill=3)
    d.polygon([(24,27),(29,27),(31,36),(26,36)], fill=3)
    d.polygon([(16,28),(18,28),(17,34),(15,34)], fill=1)
    d.polygon([(26,28),(28,28),(29,33),(27,33)], fill=1)
    d.line([(14,36),(19,36)], fill=2, width=1)
    d.line([(26,35),(31,35)], fill=2, width=1)
    d.polygon([(7,12),(7,8),(10,8),(9,3),(14,8),(18,7),(23,3),(22,10),(25,13),(24,20),(20,24),(12,24),(7,20)], fill=3)
    d.polygon([(9,12),(10,9),(12,9),(11,6),(14,10),(18,9),(21,6),(20,11),(22,13),(22,19),(19,22),(13,22),(9,19)], fill=1)
    d.polygon([(10,8),(10,5),(13,9)], fill=2)
    d.polygon([(20,9),(22,5),(21,10)], fill=2)
    d.polygon([(13,10),(14,5),(16,10)], fill=3)
    d.polygon([(17,10),(19,5),(20,11)], fill=3)
    d.line([(14,8),(15,6)], fill=1, width=1)
    d.line([(18,8),(19,6)], fill=1, width=1)
    d.rectangle((11,13,13,15), fill=3); d.point((11,13), fill=0)
    d.rectangle((18,13,20,15), fill=3); d.point((18,13), fill=0)
    d.polygon([(15,11),(16,10),(18,11),(17,12),(16,12)], fill=2)
    d.point((16,18), fill=3)
    d.line([(13,19),(16,21),(19,19)], fill=2, width=1)
    d.line([(13,23),(16,25),(19,24)], fill=2, width=2)
    return im


def back():
    im = canvas((32,32)); d = ImageDraw.Draw(im)
    d.line([(22,25),(27,22),(29,18),(28,13),(25,10),(23,10)], fill=3, width=4)
    d.line([(23,24),(26,21),(27,18),(26,14),(24,12)], fill=1, width=2)
    d.ellipse((8,14,24,27), fill=3)
    d.ellipse((10,15,22,25), fill=1)
    d.polygon([(9,23),(14,23),(13,31),(9,31)], fill=3)
    d.polygon([(18,23),(23,23),(24,31),(20,31)], fill=3)
    d.polygon([(11,24),(13,24),(12,29),(10,29)], fill=1)
    d.polygon([(20,24),(22,24),(23,29),(21,29)], fill=1)
    d.polygon([(7,10),(8,7),(10,7),(9,2),(13,6),(18,6),(22,2),(21,8),(24,11),(23,17),(20,20),(11,20),(7,17)], fill=3)
    d.polygon([(9,10),(10,8),(12,8),(11,5),(14,8),(18,8),(20,5),(19,9),(21,11),(21,16),(19,18),(12,18),(9,16)], fill=1)
    d.polygon([(13,8),(14,4),(16,8)], fill=3)
    d.polygon([(16,8),(18,4),(19,9)], fill=3)
    d.line([(11,18),(19,18),(21,20)], fill=2, width=2)
    return im


def icon():
    im = canvas((16,32)); d = ImageDraw.Draw(im)
    for frame, lift in enumerate((0,1)):
        y = frame * 16 - lift
        d.polygon([(3,7+y),(3,5+y),(5,5+y),(4,2+y),(7,5+y),(9,5+y),(12,2+y),(11,6+y),(13,8+y),(12,13+y),(9,15+y),(6,15+y),(3,12+y)], fill=3)
        d.polygon([(5,7+y),(5,6+y),(6,6+y),(6,4+y),(7,6+y),(9,6+y),(10,4+y),(10,7+y),(11,8+y),(10,12+y),(8,13+y),(6,13+y),(5,11+y)], fill=1)
        d.point((6,9+y), fill=3); d.point((9,9+y), fill=3)
        d.point((8,11+y), fill=2)
    return im


def save(im, path):
    ROOT.mkdir(parents=True, exist_ok=True)
    # Convert the four palette indices to actual grayscale luminance bytes.
    # Avoiding a PLTE chunk makes the files simpler and more robust in-game.
    pixels = bytes(SHADES[index][0] for index in im.tobytes())
    gray = Image.frombytes("L", im.size, pixels)
    out = ROOT / path
    gray.save(out, format="PNG", optimize=True)
    with Image.open(out) as check:
        check.verify()

if __name__ == "__main__":
    save(front(), "aeglet_front.png")
    save(back(), "aeglet_back.png")
    save(icon(), "aeglet_icon.png")
    print("generated and verified Aeglet assets")
