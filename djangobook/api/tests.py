from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import BookPost
from datetime import date, timedelta
from .validators import isbn_validator
from django.core.exceptions import ValidationError

class BookPostTests(APITestCase):
    def setUp(self):
        # Create some initial data for testing
        self.book1 = BookPost.objects.create(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
            publication_date="1925-04-10",
            isbn="9780743273565",
            summary="A story of the fabulously wealthy Jay Gatsby and his love for the beautiful Daisy Buchanan."
        )
        self.book2 = BookPost.objects.create(
            title="1984",
            author="George Orwell",
            publication_date="1949-06-08",
            isbn="9780451524935",
            summary="A dystopian novel about totalitarianism."
        )

    # Test listing all books
    def test_list_books(self):
        url = reverse("bookpost-view-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Check that 2 books are returned

    # Test creating a new book
    def test_create_book(self):
        url = reverse("bookpost-view-create")
        data = {
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "publication_date": "1960-07-11",
            "isbn": "9780446310789",
            "summary": "A novel about racial injustice in the American South."
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BookPost.objects.count(), 3)  # Check that a new book was created

    # Test retrieving a specific book
    def test_retrieve_book(self):
        url = reverse("update", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "The Great Gatsby")

    # Test updating a specific book
    def test_update_book(self):
        url = reverse("update", args=[self.book1.id])
        data = {
            "title": "The Great Gatsby (Updated)",
            "author": "F. Scott Fitzgerald",
            "publication_date": "1925-04-10",
            "isbn": "9780743273565",
            "summary": "Updated summary about Jay Gatsby and Daisy Buchanan."
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify that the book was updated
        updated_book = BookPost.objects.get(id=self.book1.id)
        self.assertEqual(updated_book.title, "The Great Gatsby (Updated)")
        self.assertEqual(updated_book.summary, "Updated summary about Jay Gatsby and Daisy Buchanan.")

    # Test deleting a specific book
    def test_delete_book(self):
        url = reverse("update", args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BookPost.objects.count(), 1)  # Check that one book was deleted
    
    # Test publication date validation (future date)
    def test_publication_date_future(self):
        future_date = date.today() + timedelta(days=365)  # A date in the future
        book = BookPost(
            title="Invalid Book",
            author="Invalid Author",
            publication_date=future_date,
            isbn="9780987654321",
            summary="An invalid book with a future publication date."
        )
        with self.assertRaises(ValidationError):
            book.full_clean()  # This should raise a ValidationError

class ISBNValidatorTests(APITestCase):
    # Test ISBNs that are too short
    def test_ISBN_is_too_short(self):
        with self.assertRaises(ValidationError):
            isbn_validator('123')  # Too short (3 characters)
        
        with self.assertRaises(ValidationError):
            isbn_validator('')  # Empty string

    # Test ISBNs that are too long
    def test_ISBN_is_too_long(self):
        with self.assertRaises(ValidationError):
            isbn_validator('12345678901234')  # Too long (14 characters)

    # Test ISBNs with illegal structures
    def test_ISBN_with_illegal_structures(self):
        with self.assertRaises(ValidationError):
            isbn_validator('0765348275')  # Invalid checksum

    # Test ISBNs with invalid lowercase 'y'
    def test_invalid_lowercase_y_ISBN(self):
        with self.assertRaises(ValidationError):
            isbn_validator('832070801y')  # Lowercase 'y' is invalid

    # Test ISBNs with dashes as valid separators
    def test_dashes_as_valid_separators(self):
        self.assertTrue(isbn_validator('0-765-348-276'))  # Valid ISBN-10 with dashes
        self.assertTrue(isbn_validator('0-7-6-5-3-4-8-2-7-6'))  # Valid ISBN-10 with dashes

    # Test ISBNs with spaces as valid separators
    def test_spaces_as_valid_separators(self):
        self.assertTrue(isbn_validator('0 765 348 276'))  # Valid ISBN-10 with spaces
        self.assertTrue(isbn_validator('0 7 6 5 3 4 8 2 7 6'))  # Valid ISBN-10 with spaces

    # Test ISBNs with spaces and dashes as valid separators
    def test_space_and_dash_as_valid_separators(self):
        self.assertTrue(isbn_validator('0 765-348 276'))  # Valid ISBN-10 with spaces and dashes
        self.assertTrue(isbn_validator('0 7 6 5-3 4 8 2 7 6'))  # Valid ISBN-10 with spaces and dashes

    # Test valid ISBNs
    def test_valid_ISBNs(self):
        # Valid ISBN-10
        self.assertTrue(isbn_validator('0765348276'))  # Valid ISBN-10

        # Valid ISBN-13
        self.assertTrue(isbn_validator('9780765348272'))  # Valid ISBN-13

        # Valid ISBN-10 with uppercase 'X'
        self.assertTrue(isbn_validator('832070801X'))  # Valid ISBN-10 with 'X'
