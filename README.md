# Arport Management Application

A Django-based airport management system.

## Key Features

Find the Nth Left or Right Node in an Airport Route ( create a search form)
Find the Longest Node based on duration in the Airport (display)
Find the Shortest Node based on duration Between Two Airports(display)

## Tech Stack

- Python 3.9+
- Django 4.2+
- SQLite (Default database)

`/add` home page

## Setup Instructions

```bash
# Clone the project
git clone https://github.com/shahisiiii/Arport-management.git
cd airport

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run management command
python manage.py create_user_roles

# Run migrations and start server
python manage.py migrate
python manage.py runserver


