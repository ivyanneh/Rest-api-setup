# Flask REST API

<!-- cSpell:ignore venv (added this cause an error for venv came popping up) -->

This project is a simple REST API built with Flask to manage a Product resource.

## Question/Required details in this file

- [Setting up the environment and running the API server.]
- [Testing the API endpoints manually or with the provided Python script.]
  
## Setup Instructions

### Prerequisites

- Python
- pip (Python package installer)
- Virtual environment tool

### Installation

1. **Clone the Repository:**

    ```sh
    git clone <repository_url>
    cd flask_rest_api
    ```

2. **Create and Activate Virtual Environment:**
    - On Windows:

        ```sh
        python -m venv venv
        venv\Scripts\activate
        ```

3. **Install Dependencies:**

    ```sh
    pip install Flask requests
    ```

## Running the API Server

1. **Navigate to the Project Directory:**

    ```sh
    cd flask_rest_api
    ```

2. **Run the Flask Server:**

    ```sh
    python app.py
    ```

    The server should now be running at `http://127.0.0.1:5000/`.

## Testing the API Endpoints

### Manual Testing

You can test the API endpoints using tools like `curl` or Postman.

#### POST /products

- **Endpoint:** `http://127.0.0.1:5000/products`
- **Method:** POST
- **Headers:** `Content-Type: application/json`
- **Body:**

    ```json
    {
        "name": "Product1",
        "description": "This is a test product",
        "price": 19.99
    }
    ```

- **Example using `curl`:**

    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"name": "Product1", "description": "This is a test product", "price": 19.99}' http://127.0.0.1:5000/products
    ```

#### GET /products

- **Endpoint:** `http://127.0.0.1:5000/products`
- **Method:** GET
- **Example using `curl`:**

    ```sh
    curl -X GET http://127.0.0.1:5000/products
    ```

### Testing with Python Script 

 **Do not forget to run the Python script:**

    ```sh
    python client.py
    ```

This script will add new products and retrieve the list of all products from the API.
