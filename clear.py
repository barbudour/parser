import os


def remove_empty_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Remove empty lines
    lines = [line for line in lines if line.strip() != ""]

    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(lines)


# Path to the content folder
content_folder = "content"

# Iterate through files in the content folder
for filename in os.listdir(content_folder):
    if filename.endswith(".md"):
        file_path = os.path.join(content_folder, filename)
        remove_empty_lines(file_path)
