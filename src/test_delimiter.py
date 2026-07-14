import unittest
from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestDelimiter(unittest.TestCase):
    def test_eq(self):
        italic_delimiter_expected = [
                TextNode("delimited before italics", TextType.TEXT),
                TextNode("delimited italics", TextType.ITALIC),
                TextNode("delimited after italics", TextType.TEXT)
                ]
        bold_delimiter_expected = [
                TextNode("delimited before bold", TextType.TEXT),
                TextNode("delimited bold", TextType.BOLD),
                TextNode("delimited after bold", TextType.TEXT)
                ]
        code_delimiter_expected = [
                TextNode("delimited before code", TextType.TEXT),
                TextNode("delimited code", TextType.CODE),
                TextNode("delimited after code", TextType.TEXT)
                ]
        
        italic_delimiter_test_node = TextNode("delimited before italics_delimited italics_delimited after italics", TextType.TEXT)
        bold_delimiter_test_node = TextNode("delimited before bold**delimited bold**delimited after bold", TextType.TEXT)
        code_delimiter_test_node = TextNode("delimited before code`delimited code`delimited after code", TextType.TEXT)

        italic_delimiter_test_node_delimited = split_nodes_delimiter(italic_delimiter_test_node, "_", TextType.ITALIC)
        bold_delimiter_test_node_delimited = split_nodes_delimiter(bold_delimiter_test_node, "**", TextType.BOLD)
        code_delimiter_test_node_delimited = split_nodes_delimiter(code_delimiter_test_node, "`", TextType.CODE)

        self.assertEqual(italic_delimiter_test_node_delimited, italic_delimiter_expected)
        self.assertEqual(bold_delimiter_test_node_delimited, bold_delimiter_expected)
        self.assertEqual(code_delimiter_test_node_delimited, code_delimiter_expected)
