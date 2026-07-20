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
    
    def get_all_content_files(path) -> list[file_path:str]:
        content_files = os.listdir(path)
        file_paths = []
        for file in content_files:
            if os.isfile(path):
                file_paths.append(file)
            else:
                file_paths.append(get_all_content_files(file))
        return file_paths


    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    content_files = get_all_content_files(from_path)
    #todo: go through each file present in /content/ and generate folders and indexes in /public/
    for file in content_files:
        markdown = read_file_contents(file)
        template = read_file_contents(template_path)
        html_string = markdown_to_html_node(markdown).to_html()
        page_title = extract_title(markdown)
        html_page = template.replace("{{ Title }}", page_title).replace("{{ Content }}", html_string)

        if not os.path.exists(dest_path):
            os.mkdir(dest_path)
        with open(os.path.join(dest_path, "index.html"), "w") as file:
            file.write(html_page)

