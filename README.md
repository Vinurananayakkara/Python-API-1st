# Flask REST API with SQLAlchemy and Flask-RESTful

This is a simple REST API built using Flask, Flask-RESTful, and SQLAlchemy. It provides CRUD operations for managing users.

## Features
- SQLite database integration
- User model with `id`, `name`, and `email`
- REST API with endpoints for creating, retrieving, updating, and deleting users
- Request validation using `reqparse`
- JSON responses using `marshal_with`

## Installation

1. Clone this repository:
    ```sh
    git clone <repository_url>
    cd <repository_name>
    ```

2. Create a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the API

1. Initialize the database:
    ```sh
    python
    >>> from api import app, db
    >>> with app.app_context():
    ...     db.create_all()
    ```
    Exit the Python shell after running these commands.

2. Start the Flask application:
    ```sh
    python api.py
    ```

3. The API will run on `http://127.0.0.1:5000/`.

## API Endpoints

### Base URL
```
http://127.0.0.1:5000/api/users/
```

### Get all users
**GET** `/api/users/`
```json
Response:
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com"
    }
]
```

### Get a single user by ID
**GET** `/api/users/<id>`
```json
Response:
{
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
}
```

### Create a new user
**POST** `/api/users/`
```json
Request:
{
    "name": "Jane Doe",
    "email": "jane@example.com"
}

Response:
{
    "id": 2,
    "name": "Jane Doe",
    "email": "jane@example.com"
}
```

### Update a user
**PATCH** `/api/users/<id>`
```json
Request:
{
    "name": "Jane Smith",
    "email": "jane.smith@example.com"
}

Response:
{
    "id": 2,
    "name": "Jane Smith",
    "email": "jane.smith@example.com"
}
```

### Delete a user
**DELETE** `/api/users/<id>`
```json
Response:
{
    "id": 2,
    "name": "Jane Smith",
    "email": "jane.smith@example.com"
}
```

## License
This project is licensed under the MIT License.

