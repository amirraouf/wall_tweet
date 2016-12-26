
def generate_imagename(self, imagename):
    url = "files/users/%s/%d/%s" % (self.user.username, self.id, imagename)
    return url


def validate_content(content):
    if content == "":
        from django.core.exceptions import ValidationError
        raise ValidationError("Cannot be empty")
    return content
