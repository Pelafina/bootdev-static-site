from extract_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    if not isinstance(old_nodes, list):
        old_nodes = [old_nodes]


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    # todo: extract links, after extraction split textnode text based on extracted text, create new textnodes with extracted text
    if not isinstance(old_nodes, list):
        old_nodes = [old_nodes]

    #Extracts all links from the TextNodes and saves them in a list for later use    
    extracted_links = [] 
    for node in old_nodes:
        extracted_links.append(extract_markdown_links(node.text))

    for node in old_nodes:
        for link_text in extracted_links:
            if link_text not in node.text:
                continue
            text_without_link = node.text.split(f"[{link_text[0]}]({link_text[1]})")
            new_nodes.append(
                    TextNode(text_without_link[0], TextType.TEXT),
                    TextNode(link_text[0], TextType.LINK, link_text[1])
                    )
            



