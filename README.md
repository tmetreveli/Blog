Django Blog Project
This Django project includes a blogging platform with authentication and filtering functionalities. It is designed for users to create, view, and filter blog posts based on categories. The project uses Django Rest Framework (DRF) for API construction and drf-yasg for Swagger documentation.

Features
User Authentication: Users can log in using their email address ending with @redberry.ge.
Blog Posts: Authenticated users can create and view blog posts.
Filtering: Blog posts can be filtered by one or more categories.
Swagger Documentation: API endpoints are documented and can be tested through Swagger.
Getting Started
These instructions will get your copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Python (3.8 or later)
Django (3.x or later)
Django Rest Framework
drf-yasg
Install Python and pip (Python package manager) on your system. You can download them from the official Python website.

Installation
Clone the repository
git clone https://https://github.com/tmetreveli/Blog
cd Blog

Install the required packages:
pip install -r requirements.txt

Running the Application
To run the server:

python manage.py runserver

The application will be available at http://127.0.0.1:8000/.

Using the API
Login: Send a POST request to /login/ with the user's email.
Create Blog Post: Authenticated users can POST to /blogs/ to create a new blog post.
List and Filter Blog Posts: Send a GET request to /blogs/ with optional category filters.
Swagger Documentation
Access Swagger UI at http://127.0.0.1:8000/swagger/ to view and interact with the API's endpoints.
