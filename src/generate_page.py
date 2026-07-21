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

def generate_page(from_path, template_path, dest_path, base_path):
    repo_path = base_path
    def read_file_contents(path):
        if os.path.isfile(path):
            with open(path) as file:
                return file.read()
        else:
            raise Exception(f"{path} is not a file")

    def convert_markdown_to_html_page(file):
        markdown = read_file_contents(file)
        template = read_file_contents(template_path)
        html_string = markdown_to_html_node(markdown).to_html()
        page_title = extract_title(markdown)
        html_page = template.replace("{{ Title }}", page_title).replace("{{ Content }}", html_string)
        html_page = html_page.replace('href="/', f'href="{repo_path}').replace('src="/', f'src="{repo_path}')
        return html_page
    
    def create_html_from_markdown(path_to_copy_to, content_file_path):
        if not os.path.exists(path_to_copy_to):
            os.mkdir(path_to_copy_to)
        content_files = os.listdir(content_file_path)
        for file in content_files:
            source_path = os.path.join(content_file_path, file)
            destination_path = os.path.join(path_to_copy_to, file)
            if os.path.isdir(source_path):
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path, exist_ok=True)
                create_html_from_markdown(destination_path, source_path)
            else:
                with open(os.path.join(path_to_copy_to, f"{os.path.splitext(file)[0]}.html"), "w") as new_file:
                    new_file.write(convert_markdown_to_html_page(source_path))

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    create_html_from_markdown(dest_path, from_path)
