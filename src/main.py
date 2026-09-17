try:
    from src.html_nodes.textnode import TextNode, TextType
except ModuleNotFoundError:
    from html_nodes.textnode import TextNode, TextType

from helpers.parser import split_nodes_delimiter, extract_markdown_images, text_to_textnodes

def main():
    #node = TextNode("This is text with a `code block` word", TextType.TEXT)
    #new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    nodes = text_to_textnodes(text)
    # print(nodes, "=======")
    
main()