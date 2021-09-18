#app/catalog/__init__.py

from flask import Blueprint

main = Blueprint('main',__name__, template_folder='templates')

#import at the bottom for avoiding circular referencing
from app.catalog import routes