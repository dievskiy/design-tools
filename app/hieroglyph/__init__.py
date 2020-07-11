from flask import Blueprint

bp = Blueprint('hieroglyph', __name__)

from app.hieroglyph import routes
