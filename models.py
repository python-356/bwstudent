from exts import db


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    English = db.Column(db.Integer,nullable=False)
    Python = db.Column(db.Integer,nullable=False)
    C = db.Column(db.Integer,nullable=False)
    Total_score = db.Column(db.Integer,nullable=False)

