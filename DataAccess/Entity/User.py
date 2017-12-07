"""配置(Config)"""
import sqlalchemy
import Tool.Time
from DataAccess.Entity.EntityBase import EntityBase

class User(EntityBase):
    """用户(User)"""
    __tablename__ = "User"  # 表名
    __table_args__ = {
        "mysql_engine": "InnoDB",  # 表的引擎
        "mysql_charset": "utf8",  # 表的编码格式
    }

    id = sqlalchemy.Column(
        "id", sqlalchemy.Integer, primary_key=True, autoincrement=True)
    delflag = sqlalchemy.Column("delflag", sqlalchemy.Boolean, default=False)
    adddate = sqlalchemy.Column("adddate", sqlalchemy.DateTime, nullable=False)
    # 表结构,具体更多的数据类型自行百度
    name = sqlalchemy.Column("name", sqlalchemy.String(50), nullable=False)
    password = sqlalchemy.Column("password", sqlalchemy.String(50), nullable=False)

    def __init__(self, key, rooturl, content):
        self.key = key
        self.rooturl = rooturl
        self.content = content
        self.adddate = Tool.Time.timeobj()

    def __str__(self):
        return 'User,id:%s; delflag:%s; adddate:%s ,name:%s ,password:%s' % (
            self.id, self.delflag, self.adddate, self.name, self.password)

    __repr__ = __str__
