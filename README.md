# Service cleaning file #

Restfull service for cleaning manually enter values compare to database Product ID description

### Framework ###

* FastAPI
* SQL alchemy async

### Run application in docker ###

1. Run app using docker-compose

```shell script
    docker-compose up
```

### Run application in python###

1. Create .env file and add all variables

```shell script
    DATABASE=
    DB_USER=
    DB_PASSWORD=

    DB_PORT=
    DB_HOST=

    SECRET_KEY=09d25e094fbb6nj2556c818166b7a9554b93f7099f6f0f4cgt6cf63b72e8d3e7
    ALGORITHM=HS256
```
`SECRET_KEY`  and `ALGORITHM` - needs for app running

2. Install all packages from `requirements.txt` and ran `main.py`

3. Open in a browser

```shell script
    http://0.0.0.0:8888/docs#
```

4. click method Get /product and click `try it out` 
5. Enter part_number and factory_id and click "execute"


