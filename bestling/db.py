# coding=utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

db = SQLAlchemy(app)

# 设置数据库的连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1/user'
# 设置数据库提交操作
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 新更新的，可以不写，但是会告警
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


# 定义模型类
class Role(db.Model):
    # 表名.若不指定，设置与类名相同的表  一
    __tablename__ = 'roles'
    # 调用数据库实例的Column()来定义，设置为主键
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    # 反向外键 参数：模型类名   反向引用(自定义名字)
    user = db.relationship('User', backref='role')

class User(db.Model):
    # 多
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(32))
    passwd = db.Column(db.String(40))
    # 外键
    ro = db.Column(db.Integer, db.ForeignKey('roles.id'))


if __name__ == '__main__':
    # 删除表
    db.drop_all()
    # 创建表
    db.create_all()

    #添加数据
    ro1 = Role(name='admin')
    ro2 = Role(name='fanfan')
    # 添加多条数据，加入list中
    db.session.add_all([ro1, ro2])
    # commit操作
    db.session.commit()

    user1 = User(name='shen1shen', email='113456@qq.com', passwd='11234', ro=ro1.id)
    user2 = User(name='shen2shen', email='213456@qq.com', passwd='21234', ro=ro1.id)
    user3 = User(name='shen3shen', email='313456@qq.com', passwd='31234', ro=ro2.id)
    user4 = User(name='shen4shen', email='413456@qq.com', passwd='41234', ro=ro2.id)
    user5 = User(name='shen5shen', email='513456@qq.com', passwd='51234', ro=ro1.id)

    db.session.add_all([user1, user2, user3, user4, user5])
    db.session.commit()
    app.run(debug=True)
