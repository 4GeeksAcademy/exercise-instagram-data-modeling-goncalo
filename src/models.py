import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    profile_picture = Column(String(255))
    bio = Column(String(255))
    followers_count = Column(Integer, default=0)
    following_count = Column(Integer, default=0)
    posts = relationship("Post", back_populates="user")

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table post.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('user.id'))
    image_url = Column(String(255),nullable=False)
    caption = Column(String(255))
    likes_count = Column(Integer, default=0)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    user = relationship("User",back_populates="posts")
    comments = relationship("Comment", back_populates="post")

class Comment(Base):
    # Here we define columns for the table Comment.
    # Notice that each column is also a normal Python instance attribute.
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    text = Column(String(255))
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    user = relationship("User")
    post = relationship("Post", back_populates=("comments"))

class Like(Base):
    __tablename__='like'
    # Here we define columns for the table like.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    creation_date = Column(DateTime(timezone=True), server_default=func.now())

class Share(Base):
    __tablename__ = 'share'
    # Here we define columns for the table share.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    user = relationship("User")
    post = relationship("Post")


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
