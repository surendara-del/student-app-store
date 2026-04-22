#!/bin/bash
# Start script for Render deployment
export FLASK_ENV=${FLASK_ENV:-production}
export PORT=${PORT:-8080}

# Start the Flask app with Gunicorn
gunicorn --bind 0.0.0.0:$PORT --workers 1 app:create_app