from app.home import bp
from flask import render_template
from flask import send_file
from app.forms import ToolForm
from app.hieroglyph import HieroglyphTracer as hModel

model = hModel.HieroglyphTracer()

@bp.route("/tools/hieroglyph")
def main():
    return render_template('hieroglyph/main.html', title="Hieroglyph generation")


@bp.route("/tools/hieroglyph/generate", methods=['POST'])
def generate_hieroglyph():
    """Generate hieroglyph in svg format """
    return model.get_traced_hieroglyph_svg("https://i.imgur.com/XqPWIsc.png")

#
# @bp.route('/tools')
# def save_hieroglyph():
#     return send_file(svg_filename, mimetype='image/svg+xml',
#                      as_attachment=True, attachment_filename="hieroglyph.svg")
