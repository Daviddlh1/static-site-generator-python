import re

try:
    from src.html_nodes import TextNode, TextType
except ModuleNotFoundError:
    from html_nodes import TextNode, TextType
    
def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_delimiter_neds_work(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    
    for node in old_nodes:
        open_delimiter_index = None
        text_initial_index = 0
        text = node.text
        for i in range(len(text)):
            if text[i] == delimiter and open_delimiter_index is None:
                open_delimiter_index = i
                if text_initial_index != i:
                    new_nodes.append(TextNode(text[text_initial_index : i], TextType.TEXT))
            
            if text[i] == delimiter and open_delimiter_index is not None and open_delimiter_index != i:
                print(open_delimiter_index + 1, i)
                new_nodes.append(TextNode(text[open_delimiter_index + 1: i], text_type))
                text_initial_index = i + 1
                open_delimiter_index = None
        
        if text_initial_index < len(text):
            new_nodes.append(TextNode(text[text_initial_index : len(text)], TextType.TEXT))
    
    return new_nodes

def extract_markdown_images(text):
    regex_alt = r"\[(.*?)\]"
    regex_image_link = r"\(.*?\)"
    
    alts = re.findall(regex_alt, text)
    images: list[str] = re.findall(regex_image_link, text)
    
    result: list[tuple[str, str]]= []
    for i in range(len(alts)):
        result.append((alts[i], images[i].replace("(","").replace(")","")))
    
    return result

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    
    return matches

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        text = node.text
        images = extract_markdown_images(text)
        
        if len(images) == 0:
            continue
            
        remaining_text = text
        
        for alt, link in images:
            image_markdown = f"![{alt}]({link})"
            
            sections = remaining_text.split(image_markdown, 1)
            
            if len(sections[0]) > 0:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            new_nodes.append(TextNode(alt, TextType.IMAGE, link))
            print(sections)
            if len(sections) > 2:
                remaining_text = sections[1]
            
        if len(remaining_text) > 0:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
            
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        text = node.text
        links = extract_markdown_links(text)
        
        if len(links) == 0:
            continue
        
        remaining_text = text
        
        for alt, link in links:
            link_markdown = f"[{alt}]({link})"
            sections = remaining_text.split(link_markdown, 1)
            
            if len(sections[0]) > 0:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            new_nodes.append(TextNode(alt, TextType.LINK, link))

            remaining_text = sections[1]
            
        if len(remaining_text) > 0:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    return nodes