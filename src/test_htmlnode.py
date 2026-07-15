import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode

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
        self.assertEqual(node.prop_to_html(), node2.prop_to_html())
        self.assertNotEqual(node.prop_to_html(), node3.prop_to_html())

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!")
        self.assertEqual(node.to_html(), "<a>Hello, world!</a>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_greatgrandchildren(self):
        greatchild_node = LeafNode("a", "greatchild")
        grandchild_node = ParentNode("b", [greatchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b><a>greatchild</a></b></span></div>",
        )

    def test_to_html_no_children(self):
        standalone_node = LeafNode("span", "standalone")
        self.assertEqual(
                standalone_node.to_html(),
                "<span>standalone</span>"
                )

    def test_to_html_many_children(self):
        child_node1 = LeafNode("a", "child1")
        child_node2 = LeafNode("b", "child2")
        child_node3 = LeafNode("c", "child3")
        child_node4 = LeafNode("d", "child4")
        parent_node = ParentNode("span", [child_node1, child_node2, child_node3, child_node4])
        self.assertEqual(
                parent_node.to_html(),
                "<span><a>child1</a><b>child2</b><c>child3</c><d>child4</d></span>"
                )

if __name__ == "__main__":
    unittest.main()
