# Jorvik

Django REST API backend.

## Stack

- [Django](https://www.djangoproject.com/) 6.1
- [Django REST Framework](https://www.django-rest-framework.org/) 3.18
- [django-cors-headers](https://github.com/adamchainz/django-cors-headers) 4.9
- Python 3.13+, managed with [uv](https://docs.astral.sh/uv/)

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Setup

```sh
cd backend
uv sync          # creates the virtualenv and installs dependencies
uv run manage.py migrate
```

## Run

```sh
uv run manage.py runserver
```

Dev server at <http://127.0.0.1:8000/>. `db.sqlite3` is gitignored, so run `migrate` after a fresh clone.

## Project layout

```
backend/
├── config/     # Django project (settings, urls, asgi/wsgi)
├── api/        # API app
├── manage.py
└── pyproject.toml
```

## Notes

- Early scaffold — no models or endpoints yet. DRF and CORS headers are installed but not yet wired into `INSTALLED_APPS`.
- `SECRET_KEY` in `config/settings.py` is a dev-only placeholder and `DEBUG = True`. Do not deploy as-is.
