import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is an italic text node", TextType.ITALIC)
        node4 = TextNode("This is a text node", TextType.BOLD, "wrong_url.jpeg")

        self.assertEqual(node.url, None)
        self.assertNotEqual(node.text_type, node3.text_type)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)

class TestLeafNodeConversion(unittest.TestCase):
    def test_eq(self):
        plain_node = TextNode("Plain Node", TextType.TEXT)
        bold_node = TextNode("Bold Node", TextType.BOLD)
        italics_node = TextNode("Italics Node", TextType.ITALIC)
        code_node = TextNode("Code Node", TextType.CODE)
        link_node = TextNode("Link Node", TextType.LINK, {"href":"Link in link node"})
        image_node = TextNode("Image Node", TextType.IMAGE, {"src": "image url", "alt": "alt text"})

        self.assertEqual(text_node_to_html_node(plain_node), LeafNode(None, "Plain Node"))
        self.assertEqual(text_node_to_html_node(bold_node), LeafNode("b", "Bold Node"))
        self.assertEqual(text_node_to_html_node(italics_node), LeafNode("i", "Italics Node"))
        self.assertEqual(text_node_to_html_node(code_node), LeafNode("code", "Code Node"))
        self.assertEqual(text_node_to_html_node(link_node), LeafNode("a", "Link Node", {"href":"Link in link node"}))
        self.assertEqual(text_node_to_html_node(image_node), LeafNode("Image Node", "", {"src": "image url", "alt": "alt text"}))


if __name__ == "__main__":
    unittest.main()
