from textnode import TextNode
from textnode import TextType
from copy_to_public import copy_static_to_public
from generate_page import generate_page
import os

def main():
    copy_static_to_public()
    content = os.path.abspath("./content")
    template = os.path.abspath("./template.html")
    dest_path = os.path.abspath("./public")
    generate_page(content, template, dest_path)

main()
