import unittest
from split_nodes import split_nodes_link, split_nodes_image     
from textnode import TextNode, TextType

class TestSplitNodesLink(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text with a [link](website.com) and another [link2](website2.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected_nodes = [
                TextNode("This is a text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "website.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("link2", TextType.LINK, "website2.com")
                ]
        self.assertListEqual(expected_nodes, new_nodes)

class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
            )
        new_nodes = split_nodes_image([node])
        expected_nodes = [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ]
        self.assertListEqual(expected_nodes, new_nodes)
