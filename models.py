from db import db
from datetime import datetime
import os
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """User model for login and app management"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=True)
    password_hash = db.Column(db.String(256), nullable=True)  # Nullable for OAuth users
    role = db.Column(db.String(20), default='user')
    google_id = db.Column(db.String(50), unique=True, nullable=True)
    profile_picture = db.Column(db.String(300), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return f'<User {self.username}>'


class App(db.Model):
    """App model for storing app information"""
    __tablename__ = 'apps'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    version = db.Column(db.String(20), default='1.0.0')
    category = db.Column(db.String(50), nullable=False)
    developer = db.Column(db.String(150), nullable=False)
    developer_college = db.Column(db.String(200), default='Rajalakshmi Engineering College')
    file_path = db.Column(db.String(300), nullable=False)
    file_type = db.Column(db.String(10), nullable=False)
    file_size = db.Column(db.Integer)  # in bytes
    downloads = db.Column(db.Integer, default=0)
    rating = db.Column(db.Float, default=0.0)
    rating_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    ratings = db.relationship('Rating', backref='app', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'version': self.version,
            'category': self.category,
            'developer': self.developer,
            'developer_college': self.developer_college,
            'file_type': self.file_type,
            'file_size': self.file_size,
            'downloads': self.downloads,
            'rating': round(self.rating, 1),
            'rating_count': self.rating_count,
            'created_at': self.created_at.isoformat(),
        }
    
    def __repr__(self):
        return f'<App {self.name}>'


class Rating(db.Model):
    """Rating model for app ratings"""
    __tablename__ = 'ratings'
    
    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.Integer, db.ForeignKey('apps.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1-5 stars
    review = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Rating app_id={self.app_id}, rating={self.rating}>'


class Statistics(db.Model):
    """Statistics model for tracking app store metrics"""
    __tablename__ = 'statistics'
    
    id = db.Column(db.Integer, primary_key=True)
    total_apps = db.Column(db.Integer, default=0)
    total_downloads = db.Column(db.Integer, default=0)
    active_users = db.Column(db.Integer, default=0)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Statistics apps={self.total_apps}, downloads={self.total_downloads}>'
