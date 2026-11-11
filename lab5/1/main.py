from pathlib import Path


def human_size(size):
    units = ("Б", "КБ", "МБ", "ГБ", "ТБ", "ПБ")
    value = float(size)
    unit_index = 0

    while unit_index < len(units) - 1 and round(value) >= 1024:
        value /= 1024
        unit_index += 1

    return f"{round(value)}{units[unit_index]}"


def get_files_sizes(directory=Path.cwd()):
    directory = Path(directory)
    result = []

    for item in sorted(directory.iterdir(), key=lambda path: path.name.lower()):
        if item.is_file():
            result.append(f"{item.name} {human_size(item.stat().st_size)}")

    return "\n".join(result)


if __name__ == "__main__":
    output = get_files_sizes(Path.cwd())
    if output:
        print(output)
