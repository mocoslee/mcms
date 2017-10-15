

class PopMessage(object):

    def __init__(self, message, style='info'):
        self.body = message
        self.style = style

    def css_class(self):
        return self.style


def get_filename(filename):
    return filename.upper()
