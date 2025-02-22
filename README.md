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
    # On Windows
    python -m venv venv
    source venv\Scripts\activate 
    pip install -r requirements.txt
  ```
  ```bash
    # On MacOs
    python -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt 
  ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```
5. Access the API at [http://127.0.0.1:8000/bookpost/](http://127.0.0.1:8000/bookpost/)

## Code Structure
**Models**: Defined in models.py with the BookPost model.

**Views**: Implemented in views.py using Django REST Framework's generics and APIView.

**Serializers**: Defined in serializers.py to handle data serialization and deserialization.

**Validators**: Custom validators for ISBN and publication date in validators.py.

**Tests**: Unit tests for models, views, and validators in tests.py.

## Example Test Run
### Unit Test Run
- Find the Unit tests at api/tests.py
  <br><img src= "https://github.com/user-attachments/assets/bf4c9ed1-bdaf-47e1-be65-ac3415cd9808" height="80%" width="80%" alt=""/><br>
  
### API Endpoints Run
- Get Full List
   <br><img src= "https://github.com/user-attachments/assets/b86f1610-e5cf-40c2-aadd-f3bcb6e46ac8" height="80%" width="80%" alt=""/><br>
- POST
   <br><img src= "https://github.com/user-attachments/assets/3ca88ee0-8c72-4608-9c43-965cc1b70851" height="80%" width="80%" alt=""/><br>
- DELETE by ID
   <br><img src= "https://github.com/user-attachments/assets/772531f3-7f39-4f9c-94c2-e17e723f51f4" height="80%" width="80%" alt=""/><br>
- UPDATE BY id
   <br><img src= "https://github.com/user-attachments/assets/9d10be2c-4179-4aa0-9bbe-725fc2474db4" height="80%" width="80%" alt=""/><br>
- SEARCH by title
   <br><img src= "https://github.com/user-attachments/assets/86f4e6c5-0ea9-4fc5-9304-9508a1af9762" height="80%" width="80%" alt=""/><br>
- GET by ID
  <br><img src= "https://github.com/user-attachments/assets/9823e237-2e3b-4716-b0f9-01a5e7eed92b" height="80%" width="80%" alt=""/><br>

## Key Decisions Made
### 1. Use of `generics` and `APIView` for Views
Django REST Framework's `generics` (e.g., `ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`) and `APIView` were used to implement the API endpoints. This reduced the amount of boilerplate code and made the views more maintainable.

### 2. Search Functionality Using `icontains`
The search functionality uses `icontains` to perform case-insensitive partial matching on the `title` field. This provides a more user-friendly search experience.

### 3. Use of SQLite for Development
SQLite was used as the default database for development because it is lightweight and requires no additional setup. For production, the database can be switched to PostgreSQL or MySQL.

### 4. Inclusion of Migration Files in Version Control
Migration files were included in the repository to ensure that anyone cloning the project can set up the database schema without creating new migrations.

### 5. Use of `gettext_lazy` for Translation Support
The `gettext_lazy` function was used for error messages in validators to support internationalization (i18n).

### 6. Comprehensive Unit Tests
Unit tests were written to cover models, views, and validators to ensure the application behaves as expected. This improves the reliability of the application and makes it easier to catch bugs during development.
