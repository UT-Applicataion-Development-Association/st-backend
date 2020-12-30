from flask import request, Blueprint
from json import dumps

courseRoutes = Blueprint('courseRoute', __name__)


@courseRoutes.route('/s/<course_id>', methods=['GET'])
def handler(course_id):
    return dumps({})
