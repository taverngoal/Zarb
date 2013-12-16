__author__ = 'tavern'
# coding:utf-8


from .models import *


class obj_tag(db.Model):
    __tablename__ = "abc_tags"
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.CHAR(255), nullable=False)
    memo = db.Column('memo', db.String(255), nullable=True, default='')
    count = db.Column('count', db.Integer, default=0)
    posts = db.relationship('obj_post', backref=db.backref('tag_objs'), lazy='dynamic',
                            secondary=tag_posts_Table)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'memo': self.memo,
            'count': self.count
        }
