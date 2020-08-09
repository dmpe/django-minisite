release: python3 manage.py makemigrations && python3 manage.py migrate --no-input
web: gunicorn finance.wsgi --log-file -
