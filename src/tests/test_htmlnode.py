import unittest
from src.html_nodes.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_print(self):
        node = HTMLNode("<p>", "test")
        
        self.assertIsNotNone(node)
        
    def test_HTMLNode_props_to_html_method(self):
        expected_props = 'href="https://testurl.com" target="_blank"'
        test_props = {
            "href": "https://testurl.com",
            "target": "_blank"
        }
        
        node = HTMLNode("a", "test", None, test_props)
        
        self.assertEqual(expected_props, node.props_to_html())