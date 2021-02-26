from app.hieroglyph.model import HieroglyphModel
from subprocess import call
import uuid
import os
import io
import config


class HieroglyphTracer:
    def __init__(self):
        self._model = HieroglyphModel()
        self._svg_filename = './app/tmp/' + str(uuid.uuid4()) + '.svg'
        self._svg_raw = ''
        self.potrace_path = config.Config.POTRACE_PATH

    def trace(self, stiffness):
        """
        Return raw svg code to display in html
        """
        bmp_image_file = self._model.generate_hieroglyph(stiffness)
        if not bmp_image_file:
            return ""

        call('%s %s -o %s --svg --width 5' % (self.potrace_path,
                                               bmp_image_file, self._svg_filename), shell=True)
        with open(self._svg_filename, 'r') as file:
            self._svg_raw = file.read()

        # remove svg and bmp files
        if os.path.exists(self._svg_filename):
            os.remove(self._svg_filename)
        if os.path.exists(bmp_image_file):
            os.remove(bmp_image_file)

        return self._svg_raw

    def get_traced_hieroglyph_svg(self, stiffness):
        svg_traced = self.trace(stiffness)
        if svg_traced:
            return svg_traced
        return None

    def get_svg_raw(self):
        return self._svg_raw

    def clear_data(self):
        self._svg_raw = ''
