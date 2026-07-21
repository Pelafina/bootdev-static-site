from textnode import TextNode
from textnode import TextType
from copy_to_public import copy_static_to_public
from generate_page import generate_page
import os
import sys

def main():
    base_path = "/TESTING/"
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    copy_static_to_public("docs")
    content = os.path.abspath("./content")
    template = os.path.abspath("./template.html")
    dest_path = os.path.abspath("./docs")
    generate_page(content, template, dest_path, base_path)

main()
