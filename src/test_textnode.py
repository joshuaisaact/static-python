import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is one node", TextType.CODE)
        node2 = TextNode("This is one node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_no_url(self):
        node = TextNode("This has no url", TextType.TEXT)
        self.assertEqual(node.url, None)

    def test_url(self):
        node = TextNode("This is a url", TextType.LINK, "https://www.example.com")
        self.assertEqual(node.url, "https://www.example.com")


if __name__ == "__main__":
    unittest.main()
