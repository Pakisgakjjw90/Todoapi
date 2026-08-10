# Todo API

A simple CRUD API for managing tasks built with Django and Django REST Framework.

## How to run

```bash
pip install django djangorestframework drf-spectacular
python manage.py migrate
python manage.py runserver
```

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/tasklist/ | List all tasks |
| POST | /api/tasklist/ | Create a task |
| GET | /api/task/{id}/ | Get one task |
| PUT | /api/task/{id}/ | Update a task |
| DELETE | /api/task/{id}/ | Delete a task |

## Swagger UI

Visit http://127.0.0.1:8000/api/docs/ to see interactive API docs.

## Example

```bash
curl -X POST http://127.0.0.1:8000/api/tasklist/ -H "Content-Type: application/json" -d '{"title":"Buy milk","done":false}'
```

Response:
```json
{"id": 1, "title": "Buy milk", "done": false}
```
