#app/auth/__init__.py

from flask import Blueprint

authentication = Blueprint("authentication",__name__, template_folder="templates")

#import at bottom to avoid circular reference with routes.py (which imports authentication Blueprint)
from app.auth import routes