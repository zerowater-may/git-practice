from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fcuser(db.Model):
    __tablename__ = 'fcuser'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    userid = db.Column(db.String(32))
    password = db.Column(db.String(64))

    process = db.Column(db.String(64))
    memory = db.Column(db.String(64))      
    ram = db.Column(db.String(64))
    hostname= db.Column(db.String(64))
    ip = db.Column(db.String(64))
    serial = db.Column(db.String(64))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'password': self.password,
            'userid': self.userid,
            'username': self.username,

            'process': self.process,
            'memory': self.memory,
            'ram': self.ram,
            'hostname': self.hostname,
            'ip': self.ip,
            'serial' : self.serial
        }

