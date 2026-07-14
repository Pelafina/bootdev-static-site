import unittest
from block import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_eq(self):
        paragraph = "Paragraph" 
        heading = "# Heading"
        code = """```
code
```"""
        quote = "> quote"
        unordered_list = """- List item
- List item2"""
        ordered_list = """1. Ordered item
2. Ordered item
3. Ordered item"""

        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(paragraph))
        self.assertEqual(BlockType.HEADING, block_to_block_type(heading))
        self.assertEqual(BlockType.CODE, block_to_block_type(code))
        self.assertEqual(BlockType.QUOTE, block_to_block_type(quote))
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(unordered_list))
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(ordered_list))
