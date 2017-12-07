"""账户操作"""
from flask_sqlalchemy import SQLAlchemy
from App import db
from DataAccess.Entity.User import User

def init_user():
    """初始化用户"""
    user = User(name='admin', password='123.compile')
    db.session.add(user)    
    db.session.commit()
