class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        print(f"Tag = {self.tag}, Value = {self.value}, Children = {self.children}, Props = {self.props}")

    def to_html(self):
        raise NotImplementedError()

    def prop_to_html(self):
        html_text = ""
        if self.props == None or self.props == {}:
            return ""
        for value in self.props:
            html_text += f" {value}={self.props[value]}"
        return html_text

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(self, tag, value, props)

    def __repr__(self):
        print(f"Tag = {self.tag}, Value = {self.value}, Props = {self.props}")

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value

        return f"<{self.tag} {self.super().prop_to_html()}>{self.value}</{self.tag}>"
