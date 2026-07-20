from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode 
from textnode import TextNode, text_node_to_html_node, TextType
from inline import text_to_textnodes

# def markdown_to_blocks(markdown: str) -> list[str]:
#     raw_blocks = markdown.split("\n\n")
#     blocks = []
#     for block in raw_blocks:
#         if block == "":
#             continue
#         blocks.append(block.strip())
#     return blocks
#
# def block_to_block_type(block: str) -> BlockType:
#     if block.startswith("#"):
#         return BlockType.HEADING
#     elif block.startswith(">"):
#         for i in range(len(block.split("\n")) -1):
#             if not block.split("\n")[i].startswith(">"):
#                 raise Exception("Quote Block is not formatted correctly")
#         return BlockType.QUOTE
#     elif block.startswith("-"):
#         return BlockType.UNORDERED_LIST
#     elif block.startswith("```"):
#         if block.split("\n")[-1].startswith("```"):
#             return BlockType.CODE
#         else:
#             raise Exception("Code Block is not closed")
#     elif block.startswith(f"1."):
#         for i in range(len(block.split("\n"))-1):
#             if not block.split("\n")[i].startswith(f"{i + 1}."):
#                 raise Exception("Ordered List is not formatted correctly")
#         return BlockType.ORDERED_LIST
#     else:
#         return BlockType.PARAGRAPH
#
# class BlockType(Enum):
#     PARAGRAPH = "paragraph"
#     HEADING = "heading"
#     CODE = "code"
#     QUOTE =  "quote"
#     UNORDERED_LIST = "unordered list"
#     ORDERED_LIST = "ordered list"
#
# def markdown_to_html_node(markdown) -> list[ParentNode]:
#     blocks = markdown_to_blocks(markdown)
#     block_nodes = []
#     html_blocks = []
#
#     for block in blocks:
#         block_type = block_to_block_type(block)
#         if block_type != BlockType.CODE:
#             text = block.replace("\n", " ")
#         if block_type == BlockType.CODE:
#             block_nodes.append(code_to_nodes(block))
#         elif block_type == BlockType.HEADING:
#             block_nodes.append(heading_to_parent_node(text))
#         elif block_type == BlockType.PARAGRAPH:
#             block_nodes.append(ParentNode("p", text_to_leaf_nodes(text)))
#         elif block_type == BlockType.QUOTE:
#             block_nodes.append(ParentNode("blockquote", text_to_leaf_nodes(text)))
#         elif block_type == BlockType.UNORDERED_LIST:
#             block_nodes.append(ParentNode("ul", unordered_list_to_nodes(text)))
#         elif block_type == BlockType.ORDERED_LIST:
#             block_nodes.append(ParentNode("ol", ordered_list_to_nodes(text)))
#
#     html_blocks = ParentNode("div", block_nodes)
#     return html_blocks 
#
# def heading_to_parent_node(block) -> ParentNode:
#     level = 0
#     while block[level] == "#":
#         level += 1
#     if level > 6:
#         raise Exception("Invalid Heading")
#     return ParentNode(f"h{level}", text_to_leaf_nodes(block[level +1:]))
#
# def text_to_leaf_nodes(text) -> list[LeafNode]:
#     text_nodes = text_to_textnodes(text)
#     leaf_nodes = []
#     for node in text_nodes:
#         leaf_nodes.append(text_node_to_html_node(node))
#     return leaf_nodes
#
# def ordered_list_to_nodes(block) -> list[ParentNode]:
#     list_items = []
#     for line in block.split("\n"):
#         parts = line.split(". ", 1)
#         text = parts[1]
#         children = text_to_children(text) 
#         list_items.append(ParentNode("li", children))
#     return ParentNode("ol",list_items)
#
# def unordered_list_to_nodes(block) -> list[ParentNode]:
#     list_items = []
#     for line in block.split("\n"):
#         text = line[2:]
#         children = text_to_children(text)
#         list_items.append(ParentNode("li", children))
#     return ParentNode("ol", list_items)
#
# def code_to_nodes(block) -> ParentNode:
#     stripped_block = block.removeprefix("```\n")
#     stripped_block = stripped_block.removesuffix("```")
#     return ParentNode("pre",[text_node_to_html_node(TextNode(stripped_block, TextType.CODE))])
#
# def text_to_children(text: str) -> list[HTMLNode]:
#     text_nodes = text_to_textnodes(text)
#     children = []
#     for text_node in text_nodes:
#         html_node = text_node_to_html_node(text_node)
#         children.append(html_node)
#     return children
#
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block: str) -> ParentNode:
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.OLIST:
        return olist_to_html_node(block)
    if block_type == BlockType.ULIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    raise ValueError("invalid block type")


def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block: str) -> ParentNode:
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block: str) -> ParentNode:
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block: str) -> ParentNode:
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def olist_to_html_node(block: str) -> ParentNode:
    items = block.split("\n")
    html_items = []
    for item in items:
        parts = item.split(". ", 1)
        text = parts[1]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block: str) -> ParentNode:
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block: str) -> ParentNode:
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)
