#!/bin/bash
# Automated deploy script for PythonAnywhere
# Usage: bash deploy.sh

set -e

# Activate virtualenv
source /home/bew123/recipe/myenv/bin/activate

# Go to app directory
cd /home/bew123/recipe

echo "Pulling latest code from GitHub..."
git pull

echo "Installing/updating requirements..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Applying migrations..."
python manage.py migrate

echo "Reloading PythonAnywhere web app..."
touch /var/www/bew123_pythonanywhere_com_wsgi.py

echo "Deployment complete!"
