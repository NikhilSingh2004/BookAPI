# Book Backend API

This is the backend service for the Book application, providing RESTful APIs for managing books and users.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [API Documentation](#api-documentation)

## Features

- User authentication and authorization
- CRUD operations for books
- User registration and login
- Secure token-based authentication

## Technologies Used

- **Django**: Web framework for Python
- **Django Rest Framework**: Toolkit for building Web APIs in Django
- **Django Simple JWT**: JSON Web Tokens for Django Rest Framework
- **JWT**: JSON Web Tokens for authentication
- **Docker**: Containerization

## Installation

### Prerequisites

- Docker & WSL should be available on your local machine

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/NikhilSingh2004/BookAPI.git
   cd BookAPI
   ```

2. **Build & Run Container**
   ```bash
   docker-compose up --build
   ```

## API Documentation

The Documentation is provided at https://documenter.getpostman.com/view/34873005/2sA3QsBCtB