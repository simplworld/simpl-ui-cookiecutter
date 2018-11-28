# {{ cookiecutter.project_name }}

## Python Setup (assumes Python >= 3.6, simpl-games-api and {{ cookiecutter.modelservice_slug }} servers running)

```shell
$ cd {{cookiecutter.repo_slug}}
$ mkvirtualenv {{cookiecutter.repo_slug}}
$ add2virtualenv .

$ pip install -r requirements.txt
$ ./manage.py migrate
```

## Run front end

```shell
$ ./manage.py runserver 0.0.0.0:8000
```

If you need some serious debugging help, in {{cookiecutter.app_slug}}/templates/{{cookiecutter.app_slug}}/home.html set:

```js
var AUTOBAHN_DEBUG = true;
```

Which will turn on verbose debugging of the Autobahn/Websockets to help debug interactions between the browser and model service backend.
If you do this, do NOT commit this change.

Update node_modules and run Gulp to compile JS

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
