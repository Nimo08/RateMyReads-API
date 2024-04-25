# RateMyReads API
- This project entails developing a robust Django REST API tailored for managing user accounts and meticulously organizing book preferences. It facilitates seamless user interaction through a sophisticated comment system embedded within book reviews.
- It provides endpoints for user authentication, CRUD operations on books, retrieval of top-rated and recently added books, an average of the total book ratings and commenting functionality on book entries.

## Features
- User Authentication: Includes sign-up, log-in, and account management functionalities.
- Books Management: Supports CRUD operations for books.
- Book Listing: Provides access to top-rated, recently added, an average of the total book ratings and genre-based book collections, as well as search and ordering capabilities.
- Comments: Enables users to engage in dynamic commenting on other users' book entries.


## Technologies Used
- Django: A high-level Python web framework for rapid development.
- Django REST Framework: A powerful and flexible toolkit for building Web APIs.
- Docker: Containerization platform for easy deployment and management.

## Getting Started
To get started with the project, follow these steps:

### Clone the repository:

- git clone https://github.com/username/project.git
- cd project
- Set up environment variables:
- Create a .env file in the project root directory and define the following environment variables:
makefile
- SECRET_KEY=your_secret_key
- DEBUG=True

### Install dependencies:
- pip install -r requirements.txt

### Run migrations:
- python manage.py migrate

### Create a superuser (optional):
- python manage.py createsuperuser

### Start the development server:
- python manage.py runserver

## Access the API:
- Visit http://localhost:8000/api/v1/docs/ to access the API documentation and explore available endpoints.

## Usage
- Authentication: Utilize the provided endpoints for user registration, login, and token refresh to authenticate users.
- Books CRUD: Utilize the provided endpoints to perform Create, Retrieve, Update, and Delete operations on books.
- Book Listing: Access the provided endpoints to retrieve top-rated, recently added books, average ratings, and list books by genre.
- Comments: Engage with the provided endpoints to Create, Retrieve, Update, and Delete comments on books.