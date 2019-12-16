from flask import jsonify, url_for, request
from app import db
from app.api import bp
from app.models import User
from app.api.errors import bad_request


@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    if 'username' not in data or 'email' not in data:
        return bad_request('请输入用户名和邮箱')
    if User.query.filter_by(username=data['username']).first():
        return bad_request('用户名已被用，请换个用户名')
    if User.query.filter_by(email=data['email']).first():
        return bad_request('此邮箱已被用，请换个邮箱')
    user = User()
    user.from_dict(data)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_user', id=user.id)
    return response


@bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return '', 204


@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json() or {}
    if 'username' not in data or 'email' not in data:
        return bad_request('请输入用户名和邮箱')
    if User.query.filter_by(username=data['username']).first():
        return bad_request('用户名已被用，请换个用户名')
    if User.query.filter_by(email=data['email']).first():
        return bad_request('此邮箱已被用，请换个邮箱')
    user.from_dict(data)
    db.session.commit()
    response = jsonify(user.to_dict())
    return response


@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())
