# simpl-ui-cookiecutter

[Cookiecutter](https://github.com/audreyr/cookiecutter) project template for simulation UIs.

## Usage

```shell
$ cookiecutter https://github.com/simplworld/simpl-ui-cookiecutter.git
```

## Template variables

```json
{
	"project_name": "Simulation UI",
	"repo_slug": "{{ cookiecutter.project_name.lower().replace(' ', '-') }}",
	"project_slug": "{{ cookiecutter.project_name.lower().replace(' ', '_') }}",
	"game_slug": "{{ cookiecutter.repo_slug }}",
    "modelservice_slug": "{{ cookiecutter.game_slug }}-model",
	"topic_root": "world.simpl",
	"app_slug": "frontend",
	"version": "0.1.0"
}
```

Copyright © 2018 The Wharton School,  The University of Pennsylvania 

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.