from flask import request, jsonify, abort
from . import ticket_bp
from ...models import Ticket, Mechanic
from ...extensions import db
from .schemas import ticket_schema, tickets_schema

@ticket_bp.route('/', methods=['GET'])
def get_tickets():
    return jsonify(tickets_schema.dump(Ticket.query.all()))

@ticket_bp.route('/', methods=['POST'])
def create_ticket():
    new_ticket = ticket_schema.load(request.json)
    db.session.add(new_ticket)
    db.session.commit()
    return ticket_schema.dump(new_ticket), 201

@ticket_bp.route('/<int:ticket_id>/assign-mechanic/<int:mechanic_id>', methods=['PUT'])
def assign_mechanic(ticket_id, mechanic_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    mechanic = Mechanic.query.get_or_404(mechanic_id)
    ticket.mechanic = mechanic  # assign directly
    db.session.commit()
    return ticket_schema.dump(ticket)

@ticket_bp.route('/<int:ticket_id>/remove-mechanic', methods=['PUT'])
def remove_mechanic(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    ticket.mechanic = None  # remove mechanic assignment
    db.session.commit()
    return ticket_schema.dump(ticket)
