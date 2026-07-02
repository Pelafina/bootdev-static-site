import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is an italics text node", TextType.ITALICS)
        node4 = TextNode("This is a text node", TextType.BOLD, "wrong_url.jpeg")

        self.assertEqual(node.url, None)
        self.assertNotEqual(node.text_type, node3.text_type)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)

if __name__ == "__main__":
    unittest.main()
