from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE= "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

class HTMLNode:
    def __init__(
        self, 
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict | None = None
        ) -> None:
        self.tag = tag
        self.value = value
        self. children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        
        result = ""
        
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        
        return result.strip()
    
    def __repr__(self) -> str:
        return f"""HTMLNode(tag={self.tag}
            value={self.value}
            children={self.children}
            props={self.props}
            )"""