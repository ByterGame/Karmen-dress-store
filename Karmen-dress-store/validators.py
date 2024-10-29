import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class LengthValidator:
    def __init__(self, length=8, ):
        self.length = length

    def validate(self, password, user=None):
        if len(password) < self.length:
            raise ValidationError(
                _("This password must contain at least %(length)d characters."),
                code='password_length_is_less_than_required',
                params={'length': self.length},
            )

    def get_help_text(self):
        return _(
            "This password must contain at least %(length)d characters."
            % {'length': self.length}
        )


class CharValidator(object):
    def __init__(self, alphabet=("^[a-zA-Z0-9!\"#$%&'()*+,-./:;<=>?@^_`{|}~]+$"),):
        self.alphabet = alphabet
        self.pattern = re.compile(alphabet)

    def validate(self, password, user=None):
        if self.pattern.search(password) is None:
            raise ValidationError(
                _("The password must contain only digit, letters and (!\"#$%&'()*+,-./:;<=>?@^_`{|}~)"),
                code='unsupported_character_in_password',
            )

    def get_help_text(self):
        return _(
            "The password must contain only digit, letters and (!\"#$%&'()*+,-./:;<=>?@^_`{|}~)"
        )


class VariousSymbolsValidator(object):
    def __init__(self):
        pass

    def validate(self, password, user=None):
        has_letter = re.search("^[a-zA-Z]+$", password) is not None
        has_digit = re.search("^[0-9]+$", password) is not None
        if has_letter or has_digit:
            raise ValidationError(
                _("The password must contain at least one letter and number"),
                code='presence_of_mandatory_characters',
            )

    def get_help_text(self):
        return _(
            "The password must contain at least one letter and number"
        )

