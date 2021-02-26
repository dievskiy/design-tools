from app.home import bp
from flask import render_template
from flask import send_file
from app.hieroglyph.tracer import HieroglyphTracer
from flask import jsonify, request
from flask import send_from_directory
from app.hieroglyph.converter import convert_to_png, get_raw_png
import io

tracer = HieroglyphTracer()


@bp.route("/tools/hieroglyph")
def main():
    # clear cache to prevent downloading old images
    tracer.clear_data()
    return render_template('hieroglyph/main.html', title="Hieroglyph generation")


@bp.route("/tools/hieroglyph/generate", methods=['POST'])
def generate_hieroglyph():
    """ Generate hieroglyph in svg format """
    return tracer.get_traced_hieroglyph_svg(request.form['stiffness'])


@bp.route('/tools/hieroglyph/download')
def download_hieroglyph():
    """
    Download hieroglyph
    """
    svg_raw_bytes = tracer.get_svg_raw()
    format = request.args.get('format')
    if not svg_raw_bytes:
        return render_template('errors/common_error.html', title='Error', error='Please, generate image first...')
    try:
        if format == "png":
            png_raw_bytes = get_raw_png(svg_raw_bytes)
            return send_file(png_raw_bytes, mimetype='image/png', as_attachment=True,
                             attachment_filename="hieroglyph.png", cache_timeout=-1)
        else:
            # save as svg
            return send_file(io.BytesIO(svg_raw_bytes.encode()), mimetype='image/svg+xml', as_attachment=True,
                             attachment_filename="hieroglyph.svg", cache_timeout=-1)
    except RuntimeError as e:
        print(e)
        return render_template('errors/common_error.html', error='Something went wrong...')
