from extract_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    # todo: extract links, after extraction split textnode text based on extracted text, create new textnodes with extracted text
    if not isinstance(old_nodes, list):
        old_nodes = [old_nodes]


    for node in old_nodes:
        node_text = node.text
        #Extracts all links from the TextNodes and saves them in a list for later use    
        extracted_links = extract_markdown_images(node_text) 
        for link_text in extracted_links:
            full_link_text = f"![{link_text[0]}]({link_text[1]})"

            text_without_link = node_text.split(full_link_text, 1)
            new_nodes.extend([
                    TextNode(text_without_link[0], TextType.TEXT),
                    TextNode(link_text[0], TextType.IMAGE, link_text[1])
                    ])
            node_text = node_text.replace(f"{text_without_link[0]}{full_link_text}", "")

        if len(node_text) > 0:
            new_nodes.append(TextNode(node_text, TextType.TEXT))
            
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    # todo: extract links, after extraction split textnode text based on extracted text, create new textnodes with extracted text
    if not isinstance(old_nodes, list):
        old_nodes = [old_nodes]

    for node in old_nodes:
        node_text = node.text
        extracted_links = extract_markdown_links(node_text) 
        for link_text in extracted_links:
            full_link_text = f"[{link_text[0]}]({link_text[1]})"

            text_without_link = node_text.split(full_link_text, 1)
            new_nodes.extend([
                    TextNode(text_without_link[0], TextType.TEXT),
                    TextNode(link_text[0], TextType.LINK, link_text[1])
                    ])
            node_text = node_text.replace(f"{text_without_link[0]}{full_link_text}", "")
        
        if len(node_text) > 0:
            new_nodes.append(TextNode(node_text, TextType.TEXT))
    return new_nodes


