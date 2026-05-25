# Pywallet
Pywallet is a web-application for manage your crypto wallet.

## Installation & Run
As developer you need to run `docker-compose.yml` file for starting your postgres database.

```bash
# If using docker-compose
docker-compose up pywallet_postgres -d

# If using compose plugin for docker
docker compose up pywallet_postgres -d
```

It will start postgres database with default credentials `rooted:rooted:rooted`. You can change default credentials in `docker-compose.yml` file.
If you need to specify credentials you need to create `.env` file at the project root `/pywallet/.env` and use environment variables from `docker-compose.yml` file
like as:

```env
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
...
```
and reload your docker compose

For running web-application you need to install `poetry` dependency. Look at https://python-poetry.org/
And install project dependecies via `poetry install`.

Now let start!
For starting this application as developer use
```sh
cd src && poetry run python3 __main__.py
```

it will start web-application at http://127.0.0.1:8000.
Also u can view full rest specification at http://127.0.0.1:8000/docs.

### Run in production
Okay it's simple! Just run
```bash
docker-compose up -d
#or
docker compose up -d
```

Good luck!!
