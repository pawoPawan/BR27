 #!/bin/bash

# Create necessary directories
mkdir -p static
mkdir -p templates

# Copy static files
cp ../*.css static/
cp ../*.js static/

# Copy HTML files to templates
cp ../*.html templates/

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the requirements
pip install -r requirements.txt

# Make migrations for all apps
python manage.py makemigrations accounts
python manage.py makemigrations portfolio

# Apply migrations
python manage.py migrate

# Create a superuser (uncomment to create a superuser)
# python manage.py createsuperuser

# Run the development server
python manage.py runserver