# Event Management API

The Event Management API is a Django-based application that provides a RESTful API for managing events and user authentication. This API allows users to create, view, update, and delete events, as well as register and authenticate users.

This was designed for the # Trebelle API Hackathon

## Features

- User registration and authentication
- Event creation, retrieval, updating, and deletion
- Authentication and authorization for protected endpoints
- Integration with Django Rest Framework for API development
- Use of UUIDs instead of IDs for models
- Rate limiting, input validation, and logging using Treblle (refer to documentation for specific implementation)

## Requirements

- Python 3.9
- Django 4.2.3
- Django Rest Framework 3.14.0
- Treblle (refer to documentation for installation instructions)

## Installation

1. Clone the repository:

git clone "https://github.com/Noah-droid/eventAPI.git"


2. Install the required dependencies:
   
pip install -r requirements.txt


3. Run database migrations:

python manage.py migrate


4. Start the development server:

python manage.py runserver



5. Access the API at `http://localhost:8000/`.

## API Endpoints

### User Registration
- `POST /api/register/`: Register a new user by providing username, email, and password in the request body.

### User Authentication
- `POST /api/token/`: Obtain an access token by providing username and password in the request body.

### Event Management
- `GET /api/events/`: Retrieve a list of all events.
- `POST /api/events/`: Create a new event by providing event details in the request body.
- `GET /api/events/<id>/`: Retrieve details of a specific event.
- `PUT /api/events/<id>/`: Update details of a specific event.
- `DELETE /api/events/<id>/`: Delete a specific event.

Note: `<id>` should be replaced with the UUID of the event.

## Authentication and Authorization

- The API endpoints for event management require authentication. Include the access token received from the `/api/token/` endpoint in the Authorization header of each request.
- Unauthenticated requests to protected endpoints will receive a 401 Unauthorized response.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
