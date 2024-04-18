import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy import Enum

Base = declarative_base()


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    followers = relationship('Follower', back_populates='user_from', lazy=True)
    comments = relationship('Comment', back_populates='user', lazy=True)
    posts = relationship('Post', back_populates='user', lazy=True)



class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    author = relationship('User', back_populates='comment',lazy=True)  
    post = relationship('Post', back_populates='comment',lazy=True)   

class Post(Base):
    __tablename__ = 'post'
    id= Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='post')  
    comments = relationship('Comment', back_populates='post',lazy=True)  
    media = relationship('Media', back_populates='post',lazy=True)   

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum(), nullable=False)
    url = Column(String(250))
    post_id= Column(Integer, ForeignKey('post.id'))
    post = relationship('post')
    

def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Perfecto, aquí tienes el diagrama, Campeón!")
except Exception as e:
    print("Sorry! Ha habido un problema al generar el diagrama, a la otra más y mejor.")
    raise e


r""" relaciones APUNTES:

0,1: Esta notación significa "cero a uno", 
lo que indica que un registro en una tabla 
puede estar relacionado con cero 
o un registro en otra tabla. 
Esto implica que la relación es opcional, 
pero si existe, solo puede haber una relación.

0N: Esta notación también significa 
una relación opcional "cero a muchos", 
lo que indica que un registro en una tabla 
puede estar relacionado con cero 
o más registros en otra tabla.

One-to-One (1:1): 
Este tipo de relación significa 
que un registro en una tabla 
solo puede estar relacionado 
con un registro en otra tabla y viceversa.

One-to-Many (1:N): Este tipo de relación significa 
que un registro en una tabla puede tener 
múltiples relaciones con registros en otra tabla, 
pero un registro en la segunda tabla 
solo puede tener una relación 
con un registro en la primera tabla.

Many-to-Many (N:N): Este tipo de relación 
se maneja mediante una tabla intermedia 
que registra las relaciones 
entre los registros de las dos tablas.  """