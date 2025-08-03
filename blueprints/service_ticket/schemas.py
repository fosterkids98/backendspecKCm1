from marshmallow import Schema, fields, post_load
from ...models import Ticket

class TicketSchema(Schema):
    id = fields.Int(dump_only=True)
    service_date = fields.Date()
    service_desc = fields.Str()
    VIN = fields.Int()
    customer_id = fields.Int(required=True)
    mechanic_id = fields.Int(allow_none=True)  # <-- single mechanic

    @post_load
    def make_ticket(self, data, **kwargs):
        return Ticket(**data)

ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)
