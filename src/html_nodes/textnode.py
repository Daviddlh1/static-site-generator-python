from enum import Enum
from src.html_nodes import LeafNode

class TextType(Enum):
    BOLD="Bold"
    ITALIC="talic"
    CODE="Code"
    LINK ="Link"
    IMAGE= "Image"
    TEXT="text"
    
class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, TextNode)
            and self.text == other.text 
            and self.text_type == other.text_type 
            and self.url == other.url
        )
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})" 
    
def text_node_to_html_node(node: TextNode) -> LeafNode:
        tags_dict = {
            TextType.BOLD: "b",
            TextType.ITALIC: "i",
            TextType.CODE: "code",
            TextType.IMAGE: "img",
            TextType.LINK: "a",
            TextType.TEXT: None
        }
        
        return LeafNode(tags_dict[node.text_type], node.text)