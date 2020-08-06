import cairosvg
import uuid
import io
import os

def convert_to_png(svg_raw):
    png_name = './app/tmp/' + str(uuid.uuid4()) + '.png'
    cairosvg.svg2png(bytestring=svg_raw.encode(), write_to=png_name)
    return png_name


def get_raw_png(svg_raw_bytes):
    bytes = io.BytesIO()
    png_name = convert_to_png(svg_raw_bytes)
    with open(png_name, 'rb') as f:
        bytes.write(f.read())

    bytes.seek(0)
    if os.path.exists(png_name):
        os.remove(png_name)
    return bytes