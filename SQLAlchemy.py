from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


"""
需要注意的是  在需要事先在 本地 SQLservice 中创建 test 数据库 和 user 表。
"""

#创建基类对象
Base = declarative_base()

class User(Base):
    """docstring for User"""
    __tablename__ = 'user'

    id = Column(String(20),primary_key=True)
    name = Column(String(20))
# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:admin@localhost:3306/test')

DBSession = sessionmaker(bind=engine)


#向数据库中添加记录
# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()


# #从数据库中查询数据
# session = DBSession()

# user = session.query(User).filter(User.id == '5').one()

# print('type: ',type(user))
# print('name: ',user.name)

session.close()
