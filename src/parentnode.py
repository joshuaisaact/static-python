from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("A parent must have a tag")
        elif not self.children:
            raise ValueError("A parent must have children")
        else:
            children = ""
            for child in self.children:
                children += child.to_html()
            return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"
