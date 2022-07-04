## 🚀 Getting started

- Install [Python 3.8.3](https://www.python.org/downloads/release/python-383/).
- Install [PosgreSQL Client](https://pkgs.alpinelinux.org/package/v3.3/main/x86/postgresql-client).
- Install Dependencies:
    - gcc
    - libc-dev
    - linux-headers
    - postgresql-dev
    - musl-dev
    - zlib , zlib-dev

- Update pip
```bash
$ pip install --upgrade pip
```

- Install Python required libraries from requeriments.txt
```bash
$ pip install -r requeriments.txt
```
## Migrations
This application works in communication with a PostgreSQL database, so it's necessary to run migrations from Django.

```bash
#Create migrations
python manage.py makemigrations
python manage.py flush --no-input
python manage.py migrate
#Load dummy data
python manage.py loaddata initial_data.json
```

## ▶️ Launching the project

```bash
$ python manage.py runserver 0.0.0.0:8001
```


