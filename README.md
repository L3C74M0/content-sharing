# How to Run this project


## 1. Create a Virtual Environment

First, create a virtual environment using **Python 3.12**:

```bash
python3.12 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

## 2. Install Dependencies

Install all required project dependencies:

```bash
pip install -r requirements.txt
```

## 3. Run the Project

Start the Django development server:

```bash
python manage.py runserver
```

Once the server is running, the application will be available at:

```bash
http://localhost:8000/
```

# API Documentation

The project includes Swagger and ReDoc documentation, as well as a Postman collection located inside the documentation/ folder.
The documentation/ folder also contains a Postman collection for testing the endpoints.

You can access the API documentation at the following URLs:

* http://localhost:8000/api/docs/
* http://localhost:8000/api/redoc/
* http://localhost:8000/api/schema/
