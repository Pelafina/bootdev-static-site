from split_delimiter import split_nodes_delimiter
from split_nodes import split_nodes_link, split_nodes_image
from textnode import TextNode, TextType

def text_to_textnodes(text):
    node_list = [TextNode(text, TextType.TEXT)]
    delimiters = ["**", "_", "`"]
    for delimiter in delimiters:
        if delimiter in 
        node_list = split_nodes_delimiter(node_list, delimiter, TextType.TEXT)
    node_list = split_nodes_link(node_list)
    node_list = split_nodes_image(node_list)
    return node_list

