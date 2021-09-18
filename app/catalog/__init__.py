#app/catalog/__init__.py

from flask import Blueprint

main = Blueprint('main',__name__, template_folder='templates')

#import at the bottom for avoiding circular referencing with catalog/routes.py (import main Blueprint)
from app.catalog import routes