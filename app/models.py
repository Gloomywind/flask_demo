from . import app
from . import db

class honeypot(db.Model):
    __tablesname__ = 'honeypot'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(20),nullable=False)
    disk = db.Column(db.String(20),nullable=False)
    host = db.Column(db.String(20),nullable=False)
    cpu = db.Column(db.String(20),nullable=False)
    memory = db.Column(db.String(20),nullable=False)
    ports = db.Column(db.String(20),nullable=True)
      
