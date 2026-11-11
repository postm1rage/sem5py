import argparse
import zipfile


def human_size(size):
    units = ("Б", "КБ", "МБ", "ГБ", "ТБ", "ПБ")
    value = float(size)
    unit_index = 0

    while unit_index < len(units) - 1 and round(value) >= 1024:
        value /= 1024
        unit_index += 1

    return f"{round(value)}{units[unit_index]}"


def build_tree(archive):
    tree = {}

    for info in archive.infolist():
        parts = [part for part in info.filename.replace("\\", "/").split("/") if part not in ("", ".")]
        if not parts:
            continue

        current = tree
        for part in parts[:-1]:
            current = current.setdefault(part, {})

        name = parts[-1]
        if info.is_dir():
            current.setdefault(name, {})
        else:
            current[name] = info.file_size

    return tree


def print_tree(tree, level=0):
    lines = []
    for name, value in tree.items():
        indent = "  " * level
        if isinstance(value, dict):
            lines.append(f"{indent}{name}")
            lines.extend(print_tree(value, level + 1))
        else:
            lines.append(f"{indent}{name} {human_size(value)}")
    return lines


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", help="Путь к ZIP-архиву")
    args = parser.parse_args()

    with zipfile.ZipFile(args.archive, "r") as archive:
        lines = print_tree(build_tree(archive))

    if lines:
        print("\n".join(lines))


if __name__ == "__main__":
    main()
