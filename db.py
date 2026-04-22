from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

def init_db(app):
    """Initialize the database"""
    db.init_app(app)
    with app.app_context():
        db.create_all()
        from models import User

        # Create sample users if they don't exist
        try:
            if not User.query.filter_by(username='admin').first():
                admin_user = User(username='admin', role='admin')
                admin_user.set_password('admin123')
                db.session.add(admin_user)
            
            if not User.query.filter_by(username='student').first():
                sample_user = User(username='student', role='user')
                sample_user.set_password('student123')
                db.session.add(sample_user)
            
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Note: Sample users may already exist: {e}")


def reset_db(app):
    """Reset the database (for development/testing)"""
    with app.app_context():
        db.drop_all()
        db.create_all()
