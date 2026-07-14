def markdown_to_blocks(markdown: str) -> list[str]:
    raw_blocks = markdown.split("\n")
    blocks = []
    for block in raw_blocks:
        if block != "":
            blocks.append(block.strip())
    return blocks
