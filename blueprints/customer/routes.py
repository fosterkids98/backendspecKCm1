from flask import request, jsonify, abort
from . import customer_bp
from ...models import Customer
from ...extensions import db
from .schemas import customer_schema, customers_schema

@customer_bp.route('/', methods=['GET'])
def get_customers():
    return jsonify(customers_schema.dump(Customer.query.all()))

@customer_bp.route('/<int:id>', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get_or_404(id)
    return customer_schema.dump(customer)

@customer_bp.route('/', methods=['POST'])
def create_customer():
    new_customer = customer_schema.load(request.json, session=db.session)
    db.session.add(new_customer)
    db.session.commit()
    return customer_schema.dump(new_customer), 201

@customer_bp.route('/<int:id>', methods=['PUT'])
def update_customer(id):
    customer = Customer.query.get_or_404(id)
    updated_customer = customer_schema.load(request.json, instance=customer, partial=True, session=db.session)
    db.session.commit()
    return customer_schema.dump(updated_customer)

@customer_bp.route('/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return '', 204

@customer_bp.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def test():
    return jsonify({"message": f"Method: {request.method}"}), 200
