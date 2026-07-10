from textnode import TextNode, TextType  
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    return_list = []
    delimiter_to_texttype = {
            "**" : TextType.BOLD,
            "_" : TextType.ITALIC,
            "`" : TextType.CODE,
            }
    if old_nodes.text_type != TextType.TEXT:
        return_list.append(old_nodes)
        return return_list
    if delimiter not in old_nodes.text:
        raise Exception("No valid delimiter found in text")

    split_text_list = old_nodes.text.split(delimiter)
    if len(split_text_list) != 3:
        raise Exception("No closing delimiter found in text")

    return_list = [
            TextNode(split_text_list[0], TextType.TEXT),
            TextNode(split_text_list[1], delimiter_to_texttype[delimiter]),
            TextNode(split_text_list[2], TextType.TEXT)
            ]
    
    return return_list
