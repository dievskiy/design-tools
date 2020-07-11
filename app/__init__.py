from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.hieroglyph import bp as hieroglyph_bp
    app.register_blueprint(hieroglyph_bp)

    from app.home import bp as home_bp
    app.register_blueprint(home_bp)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    return app
