# Social media

Needs to install pyenv and poetry for local running. 

### Environment

```
pyenv install 3.10.6 && 
pyenv virtualenv 3.10.6 social_media && 
pyenv local social_media && 
pyenv activate social_media &&
poetry install 
```

### Create DB

Runs create_db.sql script.

```
% psql -d postgres
postgres-# \i preparation/create_db.sql`
```

### Starts local

`python social_media/main.py`

### Env Parameters

| params        | description |
|---------------|-------------|
| DATABASE_URL  | Path to DB  |

