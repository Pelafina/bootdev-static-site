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
        node_text = node.text
        for link_text in extracted_links:
            full_link_text = f"[{link_text[0]}]({link_text[1]})"

            #if the current link is not in the current node, skip the link
            if full_link_text not in node_text:
                continue

            text_without_link = node_text.split(full_link_text, 1)
            new_nodes.append(
                    TextNode(text_without_link[0], TextType.TEXT),
                    TextNode(link_text[0], TextType.LINK, link_text[1])
                    )
            node_text = node.text.replace(f"{text_without_link[0]}{full_link_text}", "")
            extracted_links.pop(0)

            #If there are no more links in the text but theres still text left add the final piece of text to a node
            if len(extracted_links) == 0 and len(node_text) > 0:
                new_nodes.append(TextNode(node_text, TextType.LINK))
            



