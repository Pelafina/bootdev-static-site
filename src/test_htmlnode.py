import unittest
from htmlnode import HTMLNode 

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("tag", "value", ["child1", "child2"], {"key1": "value1", "key2": "value2"})
        node2 = HTMLNode("tag", "value", ["child1", "child2"], {"key1": "value1", "key2": "value2"})
        node3 = HTMLNode("tagdifferent", "value2", ["child2", "child3"], {"key3": "value3", "key4": "value4"})


        self.assertEqual(node.tag, node2.tag)
        self.assertEqual(node.value, node2.value)
        self.assertEqual(node.children, node2.children)
        self.assertEqual(node.props, node2.props)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node.tag, node3.tag)
        self.assertNotEqual(node.value, node3.value)
        self.assertNotEqual(node.children, node3.children)
        self.assertNotEqual(node.props, node3.props)

if __name__ == "__main__":
    unittest.main()
