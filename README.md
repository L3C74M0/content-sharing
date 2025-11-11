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

# How to filter the endpoints

## Endpoint `/api/media/`

Returns a list of multimedia content (videos, games, music, works, etc.).

| **Parameter** | **Type** | **Example** | **Description** |
|----------------|-----------|--------------|-----------------|
| `category` | `string` | `/api/media/?category=video` | Filters by content type (`video`, `game`, `artwork`, `music`). Case-insensitive. |
| `title` | `string` | `/api/media/?title=art` | Searches by word or fragment within the title. |
| `order_by` | `string` | `/api/media/?order_by=title` or `/api/media/?order_by=-created_at` | Sorts the results (e.g. `title`, `category`, `created_at`). Prefix with `-` for descending order. |
| `limit` | `int` | `/api/media/?limit=5` | Maximum number of results to return. |
| `offset` | `int` | `/api/media/?offset=10` | Manual pagination (number of results to skip). |

## Endpoint `/api/profiles/`

List all user profiles.

| **Parameter** | **Type** | **Example** | **Description** |
|----------------|-----------|--------------|-----------------|
| `user_id` | `int` | `/api/profiles/?user_id=3` | Filters by the user ID of the profile owner. |
| `username` | `string` | `/api/profiles/?username=juan` | Searches for profiles whose username contains “juan”. |
| `order_by` | `string` | `/api/profiles/?order_by=rating_count` | Sorts by number of ratings, date, or name. |
| `limit` | `int` | `/api/profiles/?limit=10` | Maximum number of results to return. |
| `offset` | `int` | `/api/profiles/?offset=20` | Manual pagination (number of results to skip). |

## Endpoint `/api/ratings/`

Lists all ratings.

| **Parameter** | **Type** | **Example** | **Description** |
|----------------|-----------|--------------|-----------------|
| `media_id` | `int` | `/api/ratings/?media_id=5` | Filters all ratings for a specific media item. |
| `user_id` | `int` | `/api/ratings/?user_id=2` | Filters ratings made by a specific user. |
| `min_score` | `int` | `/api/ratings/?min_score=3` | Filters ratings with a score greater than or equal to this value. |
| `max_score` | `int` | `/api/ratings/?max_score=5` | Filters ratings with a score less than or equal to this value. |
| `order_by` | `string` | `/api/ratings/?order_by=score` or `/api/ratings/?order_by=-score` | Sorts results by score, date, or ID. Prefix with `-` for descending order. |
| `limit` | `int` | `/api/ratings/?limit=10` | Maximum number of results to return. |
| `offset` | `int` | `/api/ratings/?offset=10` | Manual pagination (number of results to skip). |


# API Documentation

The project includes Swagger and ReDoc documentation, as well as a Postman collection located inside the documentation/ folder.
The documentation/ folder also contains a Postman collection for testing the endpoints.

You can access the API documentation at the following URLs when running the project:

* http://localhost:8000/api/docs/
* http://localhost:8000/api/redoc/
* http://localhost:8000/api/schema/
  
