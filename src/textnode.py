from enum import Enum
from htmlnode import LeafNode

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

    def text_node_to_html_node(text_node: TextNode) -> LeafNode:
        if self.text_type not in TextType:
            raise ValueError("Wrong TextType")
        texttype_to_tag = {
                "plain": ""
                "bold": "b"
                "italics": "i"
                "code": "code"
                }
        if self.text_type in texttype_to_tag:
            return f"<{texttype_to_tag[self.text_type]}>{self.text}</{texttype_to_tag[self.text_type]}>"
        elif self.text_type == "link":
            return f"<a>[{self.text}]({self.url})</a>"
        elif self.text_type == "image":
            return f"![{self.text}]({self.url})"

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALICS = "italics"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
