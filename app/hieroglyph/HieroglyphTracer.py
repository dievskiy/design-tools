class HieroglyphTracer:
    def __init__(self):
        pass

    def trace(self, url):
        import os
        import shutil
        import requests
        import base64

        from flask import Flask
        from flask import request
        from flask import abort
        from flask import send_file
        from subprocess import call

        input_image_file = '/tmp/input'
        bmp_image_file = '/tmp/temp.bmp'
        svg_filename = '/tmp/trace.svg'
        # Download image from URL
        response = requests.get(url, stream=True)
        with open(input_image_file, 'wb') as file:
            shutil.copyfileobj(response.raw, file)
        del response

        # Convert image to .bmp
        call('convert %s %s' % (input_image_file, bmp_image_file), shell=True)

        # Trace .bmp to .svg
        call('potrace %s -o %s --svg --width 6.5' % (bmp_image_file, svg_filename), shell=True)
        with open(svg_filename) as file:
            return file.read()
        # return send_file(svg_filename, mimetype='image/svg+xml', as_attachment=True, attachment_filename="hieroglyph.svg")

    def get_traced_hieroglyph_svg(self, image_requested):
        if not image_requested:
            return ""
        return self.trace(image_requested)

