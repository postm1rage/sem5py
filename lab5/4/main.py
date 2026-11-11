import argparse
import shutil
from datetime import datetime
from pathlib import Path


def make_reserve_arc(source, dest):
    source_path = Path(source).resolve()
    dest_path = Path(dest).resolve()

    if not source_path.is_dir():
        raise NotADirectoryError(f"Каталог не найден: {source}")

    dest_path.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder_name = source_path.name or "root"
    archive_base = dest_path / f"{folder_name}_{timestamp}"

    return shutil.make_archive(
        str(archive_base),
        "zip",
        root_dir=str(source_path.parent),
        base_dir=source_path.name or "."
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="Каталог для архивации")
    parser.add_argument("dest", help="Каталог для сохранения архива")
    args = parser.parse_args()

    print(make_reserve_arc(args.source, args.dest))


if __name__ == "__main__":
    main()
