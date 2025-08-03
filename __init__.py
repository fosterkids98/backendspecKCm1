from flask import Flask
from .extensions import db, ma
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    from .blueprints.customer import customer_bp
    from .blueprints.mechanic import mechanic_bp
    from .blueprints.service_ticket import ticket_bp

    app.register_blueprint(customer_bp)
    app.register_blueprint(mechanic_bp)
    app.register_blueprint(ticket_bp)
    
    with app.app_context():
        db.create_all()

    return app
