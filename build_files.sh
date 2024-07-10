#!/bin/bash

# Install dependencies
python3.9 -m pip install -r requirements.txt

# Apply migrations (if applicable)
python3.9 manage.py migrate

# Collect static files (if applicable)
python3.9 manage.py collectstatic --noinput
