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
