import unittest
from inline import extract_markdown_images, extract_markdown_links

class TestMarkDownExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

        matches2 = extract_markdown_images(
                "This is a text with ![image1](image1.com) and ![image2](image2.com)"
                )
        self.assertListEqual([("image1", "image1.com"), ("image2", "image2.com")], matches2)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
                "This is a text with a [link](website.com)"
                )
        self.assertListEqual([("link", "website.com")], matches)
        
        matches2 = extract_markdown_links(
                "This is a text with [link1](website1.com) and [link2](website2.com)"
                )
        self.assertListEqual([("link1", "website1.com"), ("link2", "website2.com")], matches2)
