# Social media

REST API for social media

### Environment

Need to install locally the next packages:
* poetry
* pyenv
* pyenv-virtualenv

Create virtualenv:

```
pyenv install 3.10.6 && 
pyenv virtualenv 3.10.6 social_media && 
pyenv activate social_media &&
pyenv local social_media && 
poetry install 
```

### Create DB PostgreSQL

Postgres must be installed. Runs create_db.sql script.

`psql -f preparation/create_db.sql`

### Locally run

`python ./social_media/main.py`

### Env Parameters

Copy .env.example as .env file and change parameters values

| params         | description   |
|----------------|---------------|
| DATABASE_URL   | Path to DB    |
| JWT_SECRET     | jwt secret    |
| JWT_ALGORITHM  | jwt algorithm |
