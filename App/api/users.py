from flask import jsonify, request, current_app, url_for
from . import api
from DataAccess.Entity import User


@api.route('/users/<int:userid>')
def get_user(userid):
    """根据id获取用户信息"""
    user = User.query.get_or_404(id)
    return jsonify(user.to_json())
