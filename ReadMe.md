# Recipe App Backend

This is the backend for the Recipe App project. It is built with Django and provides RESTful APIs for managing recipes.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd recipe-app-backend
   ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Setup
1. Create a `.env` file in the project root directory:
    ```plaintext
    DEBUG=True
    SECRET_KEY=<your-secret-key>
    ```
    Replace <your-secret-key> with a secure random string

2. Apply migrations:
    ```bash
    python manage.py migrate
    ```

## Running the Server
To start the deployment server, run:
    ```bash
    python manage.py runserver
    ```
    The server will start at `http://localhost:8000/`

