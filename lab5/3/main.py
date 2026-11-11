import argparse
import os
from pathlib import Path


def human_size(size):
    units = ("Б", "КБ", "МБ", "ГБ", "ТБ", "ПБ")
    value = float(size)
    unit_index = 0

    while unit_index < len(units) - 1 and round(value) >= 1024:
        value /= 1024
        unit_index += 1

    return f"{round(value)}{units[unit_index]}"


def get_path_size(path):
    path = Path(path)

    if path.is_symlink():
        return 0
    if path.is_file():
        return path.stat().st_size

    total = 0
    for current, directories, files in os.walk(path, followlinks=False):
        current_path = Path(current)
        directories[:] = [name for name in directories if not (current_path / name).is_symlink()]

        for name in files:
            file_path = current_path / name
            if file_path.is_symlink():
                continue
            try:
                total += file_path.stat().st_size
            except OSError:
                pass

    return total


def get_top_items(directory, limit=10):
    directory = Path(directory)
    items = []

    for item in directory.iterdir():
        try:
            items.append((item, get_path_size(item)))
        except OSError:
            continue

    return sorted(items, key=lambda item: (-item[1], item[0].name.lower()))[:limit]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=".", help="Каталог для анализа")
    args = parser.parse_args()

    for item, size in get_top_items(args.path):
        print(f"    {item.name:<60} - {human_size(size)}")


if __name__ == "__main__":
    main()
