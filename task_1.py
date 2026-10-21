import argparse
import shutil
import sys
from pathlib import Path


def copy_files(src: Path, dst: Path) -> None:
    """Рекурсивно копіює файли з src у підпапки dst за розширенням."""
    try:
        items = list(src.iterdir())
    except OSError as e:
        print(f"Не вдалося прочитати директорію {src}: {e}", file=sys.stderr)
        return

    for item in items:
        if item.resolve() == dst.resolve():
            continue

        if item.is_dir():
            copy_files(item, dst)
        elif item.is_file():
            ext = item.suffix.lstrip(".").lower() or "no_extension"
            target_dir = dst / ext
            try:
                target_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, target_dir / item.name)
            except OSError as e:
                print(f"Не вдалося скопіювати {item}: {e}", file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Копіює файли та сортує їх за розширенням."
    )
    parser.add_argument("source", help="шлях до вихідної директорії")
    parser.add_argument(
        "destination",
        nargs="?",
        default="dist",
        help="шлях до директорії призначення (за замовчуванням: dist)",
    )
    args = parser.parse_args()

    src = Path(args.source)
    dst = Path(args.destination)

    if not src.is_dir():
        print(f"Помилка: {src} не є директорією.", file=sys.stderr)
        sys.exit(1)

    copy_files(src, dst)
    print(f"Готово. Файли скопійовано в {dst}")


if __name__ == "__main__":
    main()
