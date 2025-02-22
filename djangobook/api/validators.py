from django.core.exceptions import ValidationError
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from stdnum import isbn
from six import string_types
from stdnum import isbn
from django.utils import timezone


def validate_publication_date(public_date):
    """Ensure the publication date is always in the past."""
    if public_date > now().date():
        raise ValidationError("The publication date must be in the past.")

    return public_date

def isbn_validator(raw_isbn):
    """
    Validate that the input is a valid ISBN (10 or 13 digits).
    - Removes hyphens and spaces.
    - Checks if the input is a string.
    - Validates the length (10 or 13 characters).
    - Validates the checksum using the `stdnum` library.
    """
    # Remove hyphens and spaces
    isbn_to_check = raw_isbn.replace('-', '').replace(' ', '')

    # Check if the input is a string
    if not isinstance(isbn_to_check, str):
        raise ValidationError(_('Invalid ISBN: Not a string'))

    # Check the length of the ISBN
    if len(isbn_to_check) not in (10, 13):
        raise ValidationError(_('Invalid ISBN: The length of the ISBN should be 10 or 13 characters'))

    # Validate the checksum using the stdnum library
    if not isbn.is_valid(isbn_to_check):
        raise ValidationError(_('Invalid ISBN: Failed checksum'))

    return True

#Keeps code clean and modular; By separating the validation logic from the
#model. And Makes it easy to reuse validator for other models.