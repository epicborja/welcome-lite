# WelcomeLite 

 WelcomeLite test.


### Set up

Turn up docker
```shell script
$ docker-compose -f docker-compose-prod.yaml up -d
```

Set up postgres db:
```shell script
$ docker-compose -f docker-compose-prod.yaml exec db psql -U admin

psql# CREATE DATABASE welcome_db WITH OWNER admin;
```

Run migrations:
```shell script
$ docker-compose -f docker-compose-prod.yaml exec web python manage.py migrate
```

And the app is ready on `http://127.0.0.1/`


# Tests

You will find a small implementation of functional tests at `functional_tests
/`. Unit tests can be found at `tests/`. Due to time limitations, I dod not
 fully performed TDD, but these could give you an insight on how I use to
  perform tests.
  
# Secrets

Obviously, on a real production project `.env-prod` wouldn't be committed to
 the repo. As I was not able to deploy directly with Heroku, I put it there
  as the fastest way for you to reproduce the app.
  
# Other implementations

With a little bit of time I'd implement Elasticsearch as search engine, and
using django's rest framework an API implementation for further development
 would be a nice to try.
