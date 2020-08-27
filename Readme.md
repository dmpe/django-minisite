# Django prototype for finance website

<https://djangoex.herokuapp.com>

[![Open in Gitpod Web IDE](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/dmpe/django-minisite)

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

## Static (JS, CSS) files handling

On production server, there is no access to the internet, hence static resources must be concatenated served within app.

```shell
cd webpack_js_css
sudo npm install
gulp # works only if all packages from package.json were installed
```

## Local Setup of Postgres

1. <https://www.postgresql.org/download/linux/ubuntu/>

1.5. Install optionally `sudo apt install pgadmin4` due to a great GUI for PG.

Launch with `pgadmin4`

2. You must change DB password, so execute

```
sudo -u postgres psql postgres

alter user postgres with password 'postgres';
```

3. In pgadmin4, create a new DB called `django`

4. Run django migrations, see above.

## Setup on gitpod.io

1. Launch gitpod from here

2. `createdb -h localhost -p 5432 -U gitpod django`

3. see `gitpod.yml`
