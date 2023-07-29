#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/stats', methods=['GET'])
def get_stats():
    """Retrieves the number of each object by type."""
    objects_count = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(objects_count)