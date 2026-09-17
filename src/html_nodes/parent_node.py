try:
    from .htmlnode import HTMLNode
except ImportError:
    from html_nodes.htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(
        self, tag: str,
        children: list[HTMLNode],
        props: dict | None = None
    ) -> None:
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag member")
        
        if self.children is None or len(self.children) == 0:
            raise ValueError("ParentNode must have at least one children")
        result = ""
        for child in self.children:
            result += child.to_html()
            
        return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"