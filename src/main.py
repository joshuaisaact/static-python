from textnode import TextNode, TextType

text_node = TextNode(
    "This is some anchor text", TextType.LINK, "https://www.google.com"
)


def main():
    print(text_node)


main()
