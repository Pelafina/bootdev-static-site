import unittest
from generate_page import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = """
# hello 
## hello 2
### hello 3
"""
        extracted_title = extract_title(md)
        self.assertEqual(extracted_title, "hello")

        md2 = """
#hello


__this is some italic text__
**this is some bolded text**
"""
        extracted_title2 = extract_title(md2)
        self.assertEqual(extracted_title2, "hello")
