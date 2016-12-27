from django.core.exceptions import ValidationError

def validate_content(content):
    """
    This is validator for content of tweet to check
    if it is more than 140 character or emtpy
    :param content:
    :return:
    """
    if content == "":
        raise ValidationError("Cannot be empty")
    elif len(content) > 140:
        raise ValidationError("Cannot be more than 140")
    return content
