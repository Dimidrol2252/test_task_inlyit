# Shop Cart Backend

This is a FastAPI-based backend service for managing a shopping cart. It includes user and item management, as well as error handling for incorrect requests.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/shop_cart_backend.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your PostgreSQL databases and update the data.py and alembic.ini files with your database URL.

4. Run migrations:
    ```bash
    alembic upgrade head
    ```

5. Run the FastAPI app:
    ```bash
    uvicorn app.main:app --reload
    ```

## Usage

You can interact with the API using Swagger UI at `http://127.0.0.1:8000/docs`.
