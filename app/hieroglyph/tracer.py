from app.hieroglyph.model import HieroglyphModel
from subprocess import call
import uuid
import os


class HieroglyphTracer:
    def __init__(self):
        self._model = HieroglyphModel()
        self._svg_filename = './app/tmp/' + str(uuid.uuid4()) + '.svg'
        self._svg_raw = ''

    def trace(self, stiffness):
        """
        Return raw svg code to display in html
        """
        # generate hieroglyph bmp image
        bmp_image_file = self._model.generate_hieroglyph(stiffness)
        if not bmp_image_file:
            return ""

        # trace to svg
        call('potrace %s -o %s --svg --width 6.5' % (bmp_image_file, self._svg_filename), shell=True)
        with open(self._svg_filename, 'r') as file:
            self._svg_raw = file.read()

        self.remove_files(bmp_image_file)

        return self._svg_raw

    def get_traced_hieroglyph_svg(self, stiffness):
        svg_traced = self.trace(stiffness)
        if svg_traced:
            return self.adapt_svg_to_html(svg_traced)
        return None

    def remove_files(self, bmp_image_file):
        # remove svg and bmp files
        if os.path.exists(self._svg_filename):
            os.remove(self._svg_filename)
        if os.path.exists(bmp_image_file):
            os.remove(bmp_image_file)

    def get_svg_raw(self):
        return self._svg_raw

    def clear_data(self):
        self._svg_raw = ''

    def adapt_svg_to_html(self, svg_traced: str):
        """
        Manually replace height and width to place into html div container
        """
        return svg_traced.replace('width="468.000000pt"', 'width="100%"').replace('height="468.000000pt"',
                                                                                  'height="100%"')
