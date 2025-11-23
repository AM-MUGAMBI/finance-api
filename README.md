Finance API

A Django REST Framework project with JWT authentication, custom user model, and a simple user management system.

Project Overview

Finance API allows users to:

Register and manage accounts

Authenticate using JWT tokens

Access protected endpoints

Store user preferences like currency

This project uses:

Python 3.12

Django 5.2

Django REST Framework

Simple JWT for authentication

Table of Contents

Features

Setup & Installation

API Endpoints

Testing

Contributing

License

Features

Custom User model with additional currency field

JWT Authentication (access & refresh tokens)

REST API for user registration

Admin interface for managing users

Ready for frontend integration

Setup & Installation

Clone the repository

git clone https://github.com/AM-MUGAMBI/finance-api.git
cd finance-api


Create a virtual environment

python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Apply migrations

python manage.py migrate


Create a superuser

python manage.py createsuperuser


Run the development server

python manage.py runserver


Visit http://127.0.0.1:8000/admin
 to access the admin panel.

API Endpoints
Endpoint	Method	Description
/auth/register/	POST	Register a new user
/auth/token/	POST	Obtain JWT tokens (access & refresh)
/auth/token/refresh/	POST	Refresh access token using refresh token
/auth/list/	GET	View all users (requires JWT token)

Example request: Register a new user

POST /auth/register/
{
  "username": "tonny",
  "email": "tonny@example.com",
  "password": "password123",
  "currency": "USD"
}

Testing

Use Postman or curl to test API endpoints.

Obtain a JWT token:

POST /auth/token/
{
  "username": "tonny",
  "password": "password123"
}


Response:

{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}


Access protected endpoints with the Authorization header:

Authorization: Bearer <access_token>

Contributing

Fork the repo

Create a branch: git checkout -b feature/YourFeature

Commit your changes: git commit -m "Add feature"

Push to branch: git push origin feature/YourFeature

Create a pull request

License

MIT License © 2025