from sqlalchemy import Column,String,create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
import json


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
    # 一对多:
    books = relationship('Book')

    def __str__(self):
        return 'user: id = %s,name = %s,books = %s' % (self.id, self.name,self.book)

    __repr__ = __str__

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20),primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20),ForeignKey('user.id'))

    #定义实例打印样式
    # def __str__(self):
    #     return 'book: id = %s,name = %s,user_id = %s' % (self.id, self.name, self.user_id)
    # __repr__ = __str__
    def __repr__(self):
       return 'book: id = %s,name = %s,user_id = %s' % (self.id, self.name, self.user_id) 
    

def tojson(self):
    if isinstance(self, User):
        return {
            'id': self.id,
            'name': self.name,
            'book': self.book
        }
    else:
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id
        }

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:admin@localhost:3306/test')

DBSession = sessionmaker(bind=engine)


#向数据库中添加记录
# 创建session对象:
# session = DBSession()
# # 创建新User对象:
# new_user = User(id='5', name='Bob')
# # 添加到session:
# session.add(new_user)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()


# #从数据库中查询数据
session = DBSession()

# user = session.query(User).filter(User.id == '5').one()
users = session.query(User).all()
print('user type :', type(users))
# print('id :',user.id)
# print('name :',user.name)
for u in users:
    # print('book type :',type(u.book))
    print(u)
print(users)
print('---------------------------'*3)

u = session.query(User).filter(User.id == '5').one()
# print(u)
print(json.dumps(users, default=tojson,indent=4))

session.close()


# session = DBSession()

# user = session.query(Book).filter(Book.id == '1').one()

# print('type: ',type(book))
# print('name: ',book.name)

# session.close()