from app import db


class Ticket(db.Model):
    pnr = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    from1 = db.Column(db.String, nullable=False)
    to1 = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    count = db.Column(db.String, nullable=False)
    type1 = db.Column(db.String, nullable=False)
    class1 = db.Column(db.String,nullable=False)
    email = db.Column(db.String, nullable=False)
    tel = db.Column(db.String, nullable=False)
    payment = db.Column(db.String, nullable=False)
