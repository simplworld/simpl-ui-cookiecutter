# {{ cookiecutter.project_name }}

## Python Setup (assumes Python 3.6, simpl-games-api and {{ cookiecutter.modelservice_slug }} servers running)

## Local Docker Setup

The `simpl-games-api` and `{{cookiecutter.modelservice_slug}}` containers need to be running before
starting `{{cookiecutter.project_slug}}`.

You also need to have a `is_staff=True` user in the simpl-games-api database that corresponds to the `SIMPL_GAMES_AUTH`
setting used here.

After you clone the repo, run:

```bash
$ docker-compose up
```

this will create the Docker image and run it.

## Local Setup Without Docker

### Install Python dependencies and create a SQLite database
```shell
$ cd {{ cookiecutter.repo_slug }}
$ mkvirtualenv {{ cookiecutter.modelservice_slug }}
$ pip install -r requirements.txt
$ ./manage.py migrate
```

### Run front end

```shell
$ ./manage.py runserver 0.0.0.0:8000
```

If you need some serious debugging help, in {{cookiecutter.app_slug}}/templates/{{cookiecutter.app_slug}}/home.html set:

```js
var AUTOBAHN_DEBUG = true;
```

Which will turn on verbose debugging of the Autobahn/Websockets to help debug interactions between the browser and model
service backend. If you do this, do NOT commit this change.

In a separate terminal, update node_modules and run Gulp to compile JS

```shell
$ cd to {{cookiecutter.repo_slug}} directory
$ npm install
$ npm start
```

## Run javascript unit tests (run outside Vagrant)

We use jest and enzyme for unit testing (see http://redux.js.org/docs/recipes/WritingTests.html)

```shell
$ npm test
```

## Debugging WAMP subscriptions and registrations

Point your browser to http://localhost:8080/monitor and open your javascript console
