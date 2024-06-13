import re
from django.core.exceptions import ValidationError


class CustomPasswordValidator:
    def validate(self, password, user=None):
        if not re.findall(r'\d', password):
            raise ValidationError(
                'The password must contain at least one digit.',
                code='password_no_digit'
            )
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                'The password must contain at least one uppercase letter.',
                code='password_no_upper'
            )
        if not re.findall('[a-z]', password):
            raise ValidationError(
                'The password must contain at least one lowercase letter.',
                code='password_no_lower'
            )
        if not re.findall('[^A-Za-z0-9]', password):
            raise ValidationError(
                'The password must contain at least one special character.',
                code='password_no_special'
            )

    def get_help_text(self):
        return (
            "Your password must contain at least one digit, one uppercase letter, "
            "one lowercase letter, and one special character."
        )