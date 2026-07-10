from enum import Enum
from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        text1 = (self.text, self.text_type, self.url)
        text2 = (other.text, other.text_type, other.url)
        if text1 == text2:
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


class TextType(Enum):
    TEXT = "plain"
    BOLD = "bold"
    ITALIC = "italics"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    texttype_to_tag = {
            TextType.TEXT: None,
            TextType.BOLD: "b",
            TextType.ITALIC: "i",
            TextType.CODE: "code",
            TextType.LINK: "a",
            TextType.IMAGE: "img",
            }
    if text_node.text_type == TextType.LINK:
        return LeafNode(texttype_to_tag[text_node.text_type], text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(texttype_to_tag[text_node.text_type], "", {"src": text_node.url, "alt": text_node.text}) 
    elif text_node.text_type in texttype_to_tag:
        return LeafNode(texttype_to_tag[text_node.text_type], text_node.text) 
    else:
        raise ValueError("wrong texttype")
