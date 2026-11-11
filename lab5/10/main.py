import argparse
from pathlib import Path


def format_text_block(frame_height, frame_width, file_name):
    try:
        if frame_height <= 0 or frame_width <= 0:
            raise ValueError("Размеры блока должны быть положительными")

        text = Path(file_name).read_text(encoding="utf-8-sig")
        formatted_lines = []

        for source_line in text.splitlines():
            if source_line == "":
                formatted_lines.append("")
            else:
                for start in range(0, len(source_line), frame_width):
                    formatted_lines.append(source_line[start:start + frame_width].strip())

            if len(formatted_lines) >= frame_height:
                break

        return "\n".join(formatted_lines[:frame_height])
    except Exception as error:
        return str(error)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--frame-height", type=int, required=True)
    parser.add_argument("--frame-width", type=int, required=True)
    parser.add_argument("file_name")
    args = parser.parse_args()

    print(format_text_block(args.frame_height, args.frame_width, args.file_name))


if __name__ == "__main__":
    main()
