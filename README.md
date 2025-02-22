# Book Management Application

This is a **Django application** that manages a list of books. It provides a RESTful API for creating, retrieving, updating, and deleting books, along with custom validation for ISBN and publication date.

## Features
- **Book Model**: Includes fields for `title`, `author`, `publication_date`, `isbn`, and `summary`.
- **API Endpoints**:
  - `GET /books/`: Retrieve a list of all books.
  - `POST /books/`: Create a new book.
  - `GET /books/{id}/`: Retrieve a specific book by ID.
  - `PUT /books/{id}/`: Update a specific book by ID.
  - `DELETE /books/{id}/`: Delete a specific book by ID.
- **Validation**:
  - Ensures the `isbn` field is unique and valid (10 or 13 digits).
  - Ensures the `publication_date` is in the past.
- **Unit Tests**: Comprehensive tests for models, views, and validators.

## Technologies Used
- **Backend**: Django, Django REST Framework
- **Database**: SQLite (default), can be configured for PostgreSQL, MySQL, etc.
- **Validation**: `stdnum` library for ISBN validation, custom validators for publication date.
- **Testing**: Django Test Framework, `APITestCase` for API testing.

## Testing
- Run the test suite to ensure everything works as expected:
  ```bash
  python manage.py test
  ```

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/Mumo01/djangobook.git
   ```

2. Set up the virtual environment and install dependencies:
  ```bash
  python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
  ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```
5. Access the API at [HTTP://127.0.0.](http://127.0.0.1:8000/bookpost/)

## Code Structure
**Models**: Defined in models.py with the BookPost model.

**Views**: Implemented in views.py using Django REST Framework's generics and APIView.

**Serializers**: Defined in serializers.py to handle data serialization and deserialization.

**Validators**: Custom validators for ISBN and publication date in validators.py.

**Tests**: Unit tests for models, views, and validators in tests.py.

## Example Test Run
