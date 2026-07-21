class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return (f"Tag = {self.tag}, Value = {self.value}, Children = {self.children}, Props = {self.props}")

    def to_html(self):
        raise NotImplementedError()

    def prop_to_html(self):
        html_text = ""
        if self.props == None or self.props == {}:
            return ""
        for value in self.props:
            html_text += f' {value}="{self.props[value]}'
        return html_text

    def __eq__(self, other):
        if other == None:
            return False
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
            return True
        else:
            return False

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return (f"Tag = {self.tag}, Value = {self.value}, Props = {self.props}")

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value

        return f"<{self.tag}{super().prop_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag")
        if self.children == None:
            raise ValueError("ParentNode must have children")

        child_text = ""
        for child in self.children:
            child_text += child.to_html() 

        return f"<{self.tag}>{child_text}</{self.tag}>"
