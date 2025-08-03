from .extensions import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.Integer)
    address = db.Column(db.String(200))
    tickets = db.relationship('Ticket', backref='customer')

class Mechanic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.Integer)
    salary = db.Column(db.Float)
    tickets = db.relationship('Ticket', backref='mechanic')

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_date = db.Column(db.Date)
    service_desc = db.Column(db.String(200))
    VIN = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    mechanic_id = db.Column(db.Integer, db.ForeignKey('mechanic.id'))