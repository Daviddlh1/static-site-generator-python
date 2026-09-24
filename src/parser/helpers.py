import re
from ..html_nodes import HTMLNode, ParentNode, BlockType, text_node_to_html_node


def get_heading_level(block: str) -> int:
    match = re.search(r"\#{1,6} ", block)
    if match is not None:
        matched_string = match.group(0)
        return len(matched_string) - 1
    
    return 0
        
    

def block_to_html_node(block: str, type: BlockType) -> HTMLNode:
    from .parser_functions import text_to_textnodes
    from ..html_nodes import TextType, TextNode

    match type:
        case BlockType.HEADING:
            heading_level = get_heading_level(block)
            if heading_level == 0:
                raise Exception("heading level is equal to 0")
            children_text_nodes = text_to_textnodes(block[heading_level + 1:])
            children = list(map(text_node_to_html_node, children_text_nodes))
            return ParentNode(f"h{heading_level}", children)
        case BlockType.QUOTE:
            text = "\n".join(line[1:].lstrip() for line in block.split("\n"))
            children = list(map(text_node_to_html_node, text_to_textnodes(text)))
            return ParentNode("blockquote", children)
        case BlockType.UNORDERED_LIST:
            items = [line[2:] for line in block.split("\n")]
            children = [
                ParentNode("li", list(map(text_node_to_html_node, text_to_textnodes(item))))
                for item in items
            ]
            return ParentNode("ul", children)
        case BlockType.ORDERED_LIST:
            items = [line.split(". ", 1)[1] for line in block.split("\n")]
            children = [
                ParentNode("li", list(map(text_node_to_html_node, text_to_textnodes(item))))
                for item in items
            ]
            return ParentNode("ol", children)
        case BlockType.PARAGRAPH:
            lines = block.split("\n")
            text = "\n".join(lines)
            children = list(map(text_node_to_html_node, text_to_textnodes(text)))
            return ParentNode("p", children)
        case BlockType.CODE:
            text = block[3:-3].lstrip("\n").rstrip("\n")
            return ParentNode("pre", [text_node_to_html_node(TextNode(text, TextType.CODE))])