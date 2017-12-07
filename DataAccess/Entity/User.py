from datetime import datetime
from App import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    delflag = db.Column(db.Boolean, default=False)
    addtime = db.Column(db.DateTime(), default=datetime.utcnow)
    name = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))

    def __repr__(self):
        return '<User %r>' % self.name

    def to_json(self):
        json_user = {
            'id': self.id,
            'delflag': self.delflag,
            'addtime': self.addtime,
            'name': self.name,
            'password': self.password,
        }
        return json_user
