import os
from block import markdown_to_html_node

def extract_title(markdown):
    split_markdown = markdown.strip().split("\n")
    if split_markdown[0].startswith("#"):
        if split_markdown[0].startswith("##"):
            raise Exception("No H1 header found")
        else:
            return split_markdown[0].strip("#").strip()
    else:
        raise Exception("No H1 header found")

def generate_page(from_path, template_path, dest_path):
    def read_file_contents(path):
        if os.path.isfile(path):
            with open(path) as file:
                return file.read()
        else:
            raise Exception(f"{path} is not a file")

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = read_file_contents(from_path)
    template = read_file_contents(template_path)
    html_string = markdown_to_html_node(markdown).to_html()
    page_title = extract_title(markdown)
    html_page = template.replace("{{ Title }}", page_title).replace("{{ Content }}", html_string)

    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    with open(os.path.join(dest_path, "index.html"), "w") as file:
        file.write(html_page)

