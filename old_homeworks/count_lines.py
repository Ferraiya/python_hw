def count_lines(file_path: str) -> int:
    with open(file_path, 'r', encoding='utf-8') as f:
        return len(f.readlines())

file_path = r"b_file.txt"
