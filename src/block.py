from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode 
from textnode import TextNode

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
        print(block)
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

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_blocks = []

    for block in blocks:
        if block_to_block_type(block) == BlockType.HEADING:
            html_blocks.append(ParentNode(block)
        if block_to_block_type(block) == BlockType.PARAGRAPH:
            html_blocks.append(LeafNode("<p>", block, ))
