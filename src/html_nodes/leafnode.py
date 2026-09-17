try:
    from .htmlnode import HTMLNode
except ImportError:
    from html_nodes.htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str| None, value: str, props: dict | None = None) -> None:
        super().__init__(tag, value, None, props)
        
    def to_html(self)-> str:
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        
        if self.tag is None:
            return self.value
        
        props_to_html = " " + self.props_to_html() if self.props is not None else ""
        
        return f"<{self.tag}{props_to_html}>{self.value}</{self.tag}>"
    
    def __repr__(self) -> str:
        return f"""HTMLNode(tag={self.tag}
            value={self.value}
            props={self.props}
            )"""