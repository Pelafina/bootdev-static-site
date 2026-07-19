from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode 
from textnode import TextNode, text_node_to_html_node, TextType
from inline import text_to_textnodes

def markdown_to_blocks(markdown: str) -> list[str]:
    raw_blocks = markdown.split("\n\n")
    blocks = []
    for block in raw_blocks:
        if block == "":
            continue
        blocks.append(block.strip())
    return blocks

def block_to_block_type(block: str) -> BlockType:
    if block.startswith("#"):
        return BlockType.HEADING
    elif block.startswith(">"):
        for i in range(len(block.split("\n")) -1):
            if not block.split("\n")[i].startswith(">"):
                raise Exception("Quote Block is not formatted correctly")
        return BlockType.QUOTE
    elif block.startswith("-"):
        return BlockType.UNORDERED_LIST
    elif block.startswith("```"):
        if block.split("\n")[-1].startswith("```"):
            return BlockType.CODE
        else:
            raise Exception("Code Block is not closed")
    elif block.startswith(f"1."):
        for i in range(len(block.split("\n"))-1):
            if not block.split("\n")[i].startswith(f"{i + 1}."):
                raise Exception("Ordered List is not formatted correctly")
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE =  "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def markdown_to_html_node(markdown) -> list[ParentNode]:
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    html_blocks = []

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type != BlockType.CODE:
            text = block.replace("\n", " ")
        if block_type == BlockType.CODE:
            block_nodes.append(code_to_nodes(block))
        elif block_type == BlockType.HEADING:
            block_nodes.append(heading_to_parent_node(text))
        elif block_type == BlockType.PARAGRAPH:
            block_nodes.append(ParentNode("p", text_to_leaf_nodes(text)))
        elif block_type == BlockType.QUOTE:
            block_nodes.append(ParentNode("blockquote", text_to_leaf_nodes(text)))
        elif block_type == BlockType.UNORDERED_LIST:
            block_nodes.append(ParentNode("ul", unordered_list_to_nodes(text)))
        elif block_type == BlockType.ORDERED_LIST:
            block_nodes.append(ParentNode("ol", ordered_list_to_nodes(text)))

    html_blocks = ParentNode("div", block_nodes)
    return html_blocks 

def heading_to_parent_node(block) -> ParentNode:
    level = 0
    while block[level] == "#":
        level += 1
    if level > 6:
        raise Exception("Invalid Heading")
    return ParentNode(f"h{level}", text_to_leaf_nodes(block[level +1:]))


def text_to_leaf_nodes(text) -> list[LeafNode]:
    text_nodes = text_to_textnodes(text)
    leaf_nodes = []
    for node in text_nodes:
        leaf_nodes.append(text_node_to_html_node(node))
    return leaf_nodes

def ordered_list_to_nodes(block) -> list[ParentNode]:
    list_items = []
    for line in block:
        list_items.append(ParentNode("li",text_to_leaf_nodes(line[line.index(".") + 2])))
    return list_items

def unordered_list_to_nodes(block) -> list[ParentNode]:
    list_items = []
    for line in block:
        list_items.append(ParentNode("li",text_to_leaf_nodes(line[2:])))
    return list_items

def code_to_nodes(block) -> ParentNode:
    stripped_block = block.removeprefix("```\n")
    stripped_block = stripped_block.removesuffix("```")
    return ParentNode("pre",[text_node_to_html_node(TextNode(stripped_block, TextType.CODE))])
