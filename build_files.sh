#!/bin/bash

# Ensure pip is installed
if ! command -v pip &> /dev/null
then
    echo "pip could not be found, installing now..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3.9 get-pip.py
    rm get-pip.py
fi

# Install dependencies
python3.9 -m pip install -r requirements.txt

# Set correct permissions for the SQLite database
chmod 664 /tmp/db.sqlite3
chown www-data:www-data /tmp/db.sqlite3

# Apply migrations
python3.9 manage.py migrate

python3.9 manage.py makemigrations

python3.9 manage.py migrate  

# Collect static files
python3.9 manage.py collectstatic --noinput
