release: python manage.py makemigrations && python manage.py migrate

web: gunicorn job_API.wsgi
