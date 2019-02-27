from app import db, ma
from marshmallow import fields
from .base import BaseModel, BaseSchema
from .user import User, UserSchema

class Stop(db.Model):

    __tablename__ = 'stop'

    crawl_id = db.Column(db.Integer, db.ForeignKey('crawls.id'), primary_key=True)
    bar_id = db.Column(db.Integer, db.ForeignKey('bars.id'), primary_key=True)
    bar = db.relationship('Bar')
    order = db.Column(db.Integer, nullable=False)


class Crawl(db.Model, BaseModel):

    __tablename__ = 'crawls'

    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(400), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    creator = db.relationship('User', backref='created_crawls')
    bars = db.relationship('Stop', backref='crawls')


class CrawlSchema(ma.ModelSchema, BaseSchema):

    creator = fields.Nested('UserSchema', only=('username', ))
    bars = fields.Nested('BarSchema', many=True, exclude=('bar', 'crawls'))

    class Meta:
        model = Crawl

        exclude = ('crawls', )