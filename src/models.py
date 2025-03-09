import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine,ForeignKey,Enum
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    firstname: Mapped[str] = mapped_column(nullable=False)
    lastname: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)

    comments = relationship('Comment')
    posts = relationship('Post')
    followers = relationship('Follewer')
    following = relationship('Follewer')

class Follower(Base):
    __tablename__='follewer'

    user_from_id: Mapped[int]= mapped_column(primary_key=True)
    user_to_id: Mapped[int] = mapped_column()  

    follower: Mapped[int] = mapped_column(ForeignKey('user.id'))
    followed: Mapped[int] = mapped_column(ForeignKey('user.id'))

class Post(Base):
    __tablename__= 'post'

    id: Mapped[int] = mapped_column(primary_key=True)
    users_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    user = relationship('User', back_populates='posts')
    comments  = relationship('Comment')
    media  = relationship('Media')


class Comment(Base):
    __tablename__ = 'comment'
    id: Mapped[int] = mapped_column(primary_key= True)
    comment_text: Mapped[str] =mapped_column(nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'))

    user = relationship('User', back_populates='comments')
    post = relationship('Post', back_populates='comments')

class Media(Base):
    __tablename__ = 'Media'

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column()
    url: Mapped[str] = mapped_column()
    post_id: Mapped[int]=mapped_column(ForeignKey('post.id'))

    post = relationship('Post')



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
