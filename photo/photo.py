import random
from bisect import bisect

from PIL import Image

GREYSCALE = [
    " ",
    " ",
    ".,-",
    "_ivc=!/|\\~",
    "gjez2]/(YL)t[+T7Vf",
    "mdK4ZGbNDXY5P*Q",
    "W8KMA",
    "#%$",
]

ZONEBOUNDS = [36, 72, 108, 144, 180, 216, 252]


def convert_photo(
    image_path: str = "creationofAdam.jpg",
    width: int = 260,
    height: int = 90,
) -> None:
    im = Image.open(image_path, mode="r")
    im = im.resize((width, height), Image.BILINEAR)  # 800, 190
    im = im.convert("L")  # convert to mono

    str = ""
    for y in range(0, im.size[1]):
        for x in range(0, im.size[0]):
            lum = 255 - im.getpixel((x, y))
            row = bisect(ZONEBOUNDS, lum)
            possibles = GREYSCALE[row]
            str = str + possibles[random.randint(0, len(possibles) - 1)]
        str = str + "\n"

    print(str)
