from flask import jsonify
from app.api import bp


@bp.route('/hello', methods=['GET'])
def ping():
    return jsonify('hello, world')
