from __future__ import annotations

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "assets"

SOURCES = [
    (
        Path("/Users/liyaotang/Desktop/4ed57f20-94e0-4334-ab76-a70bc25e34e3.png"),
        "hly-logo-mark-transparent.png",
        80,
        (28, 28, 26),
    ),
    (
        Path("/Users/liyaotang/Desktop/4ed57f20-94e0-4334-ab76-a70bc25e34e3.png"),
        "hly-logo-mark-white-transparent.png",
        80,
        (255, 255, 255),
    ),
    (
        Path("/Users/liyaotang/Desktop/4ed57f20-94e0-4334-ab76-a70bc25e34e3.png"),
        "hly-logo-mark-white-tight-transparent.png",
        8,
        (255, 255, 255),
    ),
    (
        Path("/Users/liyaotang/Downloads/cce805ac-3224-411d-a8bc-593d4fae137e.png"),
        "hly-logo-construction-transparent.png",
        70,
        (28, 28, 26),
    ),
]


def remove_white_background(
    source: Path,
    destination: Path,
    padding: int,
    color: tuple[int, int, int],
) -> None:
    image = Image.open(source).convert("RGBA")
    transparent = Image.new("RGBA", image.size)
    pixels: list[tuple[int, int, int, int]] = []
    source_alpha_channel = image.getchannel("A")
    alpha_min, alpha_max = source_alpha_channel.getextrema()
    has_source_transparency = alpha_min < 250 and alpha_max > 0

    for red, green, blue, source_alpha in image.getdata():
        if source_alpha < 8:
            pixels.append((*color, 0))
            continue

        if has_source_transparency:
            alpha = source_alpha
        else:
            luminance = int(0.299 * red + 0.587 * green + 0.114 * blue)
            alpha = max(0, min(255, int((244 - luminance) * 8)))
            if alpha < 8:
                alpha = 0
            alpha = min(alpha, source_alpha)
        pixels.append((*color, alpha))

    transparent.putdata(pixels)
    alpha = transparent.getchannel("A")
    bbox = alpha.getbbox()

    if bbox:
        left, top, right, bottom = bbox
        left = max(0, left - padding)
        top = max(0, top - padding)
        right = min(transparent.width, right + padding)
        bottom = min(transparent.height, bottom + padding)
        transparent = transparent.crop((left, top, right, bottom))

    transparent.save(destination)


def main() -> None:
    ASSET_DIR.mkdir(exist_ok=True)
    for source, filename, padding, color in SOURCES:
        destination = ASSET_DIR / filename
        remove_white_background(source, destination, padding, color)
        with Image.open(destination) as output:
            corners = [
                output.getpixel((0, 0))[3],
                output.getpixel((output.width - 1, 0))[3],
                output.getpixel((0, output.height - 1))[3],
                output.getpixel((output.width - 1, output.height - 1))[3],
            ]
            print(f"{destination}: {output.size}, corner alpha={corners}")


if __name__ == "__main__":
    main()
