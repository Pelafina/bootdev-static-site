from extract_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    if not isinstance(old_nodes, list):
        old_nodes = [old_nodes]


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    # todo: extract links, after extraction split textnode text based on extracted text, create new textnodes with extracted text
    if not isinstance(old_nodes, list):
        old_nodes = [old_nodes]
    
    extracted_links = extract_markdown_links(old_nodes)


