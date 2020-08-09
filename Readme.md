Run django migrations:

```
heroku run python3 manage.py makemigrations
heroku run python3 manage.py migrate
```


Or if it doesn work:

```
heroku run bash
python3 manage.py makemigrations
python3 manage.py migrate
```
