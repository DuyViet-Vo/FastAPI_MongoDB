# FastAPI MongoDB Project

This project is a template for building a RESTful API using FastAPI and MongoDB.

## Features

- FastAPI for building the API
- MongoDB for the database
- Pydantic for data validation
- Asynchronous programming with `asyncio`

## Requirements

- Python 3.12+
- MongoDB

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/fastapi-mongodb.git
    cd fastapi-mongodb
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Start MongoDB:
    ```bash
    mongod
    ```

5. Run the application:
    ```bash
    uvicorn app.main:app --reload
    ```

## Usage

Once the application is running, you can access the API documentation at `http://127.0.0.1:8000/docs`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.