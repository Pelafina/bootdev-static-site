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
            html_text += f" {self.props[value].keys()}={self.props[value]}"
        return html_text
