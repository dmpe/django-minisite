# Django prototype for finance website

<https://djangoex.herokuapp.com>

## Run DJango migrations

```shell
heroku run python3 manage.py makemigrations
heroku run python3 manage.py migrate
```

Or if it doesn't work:

```shell
heroku run bash
python3 manage.py makemigrations
python3 manage.py migrate
```

# Static (JS, CSS) files handling

On production server, there is no access to the internet, hence static resources must be concatenated served within app.

```shell
cd webpack_js_css
sudo npm install
gulp # works only if all packages from package.json were installed
```
