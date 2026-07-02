from enum import Enum

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        text1 = (self.text, self.text_type, self.url)
        text2 = (other.text, other.text_type, other.url)
        if text1 == text2:
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALICS = "italics"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
