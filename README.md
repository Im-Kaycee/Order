# Military Order System

A secure backend system for military units to manage and distribute duty rosters, routine orders, and internal communications between personnel.

## Overview

**Order** is a backend application designed to streamline communication within military units by providing a secure platform for commanders and senior personnel to disseminate information to their deployed units. The system implements role-based access control to ensure appropriate information flow while maintaining operational security.

## Features

- Secure order distribution and management
- Role-based access control with granular permissions
- Anonymous messaging system for confidential communications
- User authentication and authorization
- RESTful API architecture

## Access Control

The system implements three distinct user roles with specific permissions:

### Commander
- Post orders and duty rosters
- Receive anonymous messages from unit personnel
- View all posted orders

### Regimental Sergeant Major (RSM)
- Post orders and duty rosters
- Send anonymous messages
- View all posted orders

### Soldier
- Read all orders and duty rosters
- Send anonymous messages to commanders
- View order history

## Technical Stack

- **Framework**: Django / Django REST Framework
- **Database**: SQLite
- **Authentication**: JWT-based authentication
- **API**: RESTful architecture

## Installation

### Prerequisites

- Python 3.11 or higher
- pip package manager
- virtualenv (recommended)

### Setup Instructions

1. Clone the repository
   ```bash
   git clone <repository-url>
   cd order
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional)
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000`

## API Documentation

API documentation is available at `/api/docs/` when running the development server.

## Security Considerations

- All endpoints require authentication
- Role-based permissions enforce access control
- Anonymous messages are not traceable to sender
- Secure token-based authentication implemented

## Development Notes

This project was developed as an educational tool for a school project. As such, certain development artifacts (database files, superuser creation scripts) have been included in the repository for demonstration purposes. In a production environment, these files should be excluded from version control.
