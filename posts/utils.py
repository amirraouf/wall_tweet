
def generate_image_name(self, image_name):
    """
    This method for generation of
    :param self:
    :param image_name:
    :return:
    """
    url = "media/posts/%s/%s" % (self.user.username, image_name)
    return url
