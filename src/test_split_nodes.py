import unittest
from inline import split_nodes_link, split_nodes_image     
from textnode import TextNode, TextType

class TestSplitNodesLink(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text with a [link](website.com) and another [link2](website2.com)", TextType.TEXT)
        node2 = TextNode("This is a 2nd text with a [link3](website3.com) and [link4](website4.com) and some extra text", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        new_nodes2 = split_nodes_link([node2])
        new_nodes3 = split_nodes_link([node, node2])
        expected_nodes = [
                TextNode("This is a text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "website.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("link2", TextType.LINK, "website2.com")
                ]
        expected_nodes2 = [
                TextNode("This is a 2nd text with a ", TextType.TEXT),
                TextNode("link3", TextType.LINK, "website3.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("link4", TextType.LINK, "website4.com"),
                TextNode(" and some extra text", TextType.TEXT)
                ]
        expected_nodes3 = expected_nodes + expected_nodes2
        self.assertListEqual(expected_nodes, new_nodes)
        self.assertListEqual(expected_nodes2, new_nodes2)
        self.assertListEqual(expected_nodes3, new_nodes3)

class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
            )
        node2 = TextNode("This is a 2nd text with an ![image3](https://i.imgur.com/zjjcJKZ.png) and another ![image4](https://i.imgur.com/3elNhQu.png) and some extra text", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        new_nodes2 = split_nodes_image([node2])
        new_nodes3 = split_nodes_image([node, node2])
        expected_nodes = [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ]
        expected_nodes2 = [
                TextNode("This is a 2nd text with an ", TextType.TEXT),
                TextNode("image3", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("image4", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                TextNode(" and some extra text", TextType.TEXT)
            ]
        expected_nodes3 = expected_nodes + expected_nodes2
        self.assertListEqual(expected_nodes, new_nodes)
        self.assertListEqual(expected_nodes2, new_nodes2)
        self.assertListEqual(expected_nodes3, new_nodes3)
