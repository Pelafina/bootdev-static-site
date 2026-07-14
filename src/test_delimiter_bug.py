from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter
def main():
    nodes = [TextNode("This is **text** with an italic word", TextType.TEXT)]
    result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    for node in result:
        print(node)

main()
