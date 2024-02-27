<<<<<<< HEAD
#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Wildcard import is still expected
from api.v1.views.index import *
from api.v1.views.amenities import *
from api.v1.views.users import *
=======
#!/usr/bin/python3
"""
views
"""

from flask import Blueprint

app_views = Blueprint('/api/v1', __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.amenities import *
from api.v1.views.cities import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
from api.v1.views.users import *
from api.v1.views.places_amenities import *
>>>>>>> 2705fa05e1540f556833dcb730f7ae743b654113
