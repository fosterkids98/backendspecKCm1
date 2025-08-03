from flask import request, jsonify, abort
from . import mechanic_bp
from ...models import Mechanic
from ...extensions import db
from .schemas import mechanic_schema, mechanics_schema


@mechanic_bp.route('/', methods=['GET'])
def get_mechanics():
    return jsonify(mechanics_schema.dump(Mechanic.query.all()))

@mechanic_bp.route('/', methods=['POST'])
def create_mechanic():
    new_mechanic = mechanic_schema.load(request.json, session=db.session)
    db.session.add(new_mechanic)
    db.session.commit()
    return mechanic_schema.dump(new_mechanic), 201

@mechanic_bp.route('/<int:id>', methods=['PUT'])
def update_mechanic(id):
    mechanic = Mechanic.query.get_or_404(id)
    updated_mechanic = mechanic_schema.load(request.json, instance=mechanic, partial=True, session=db.session)
    db.session.commit()
    return mechanic_schema.dump(updated_mechanic)

@mechanic_bp.route('/<int:id>', methods=['DELETE'])
def delete_mechanic(id):
    mechanic = Mechanic.query.get_or_404(id)
    db.session.delete(mechanic)
    db.session.commit()
    return '', 204
