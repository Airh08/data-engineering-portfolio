from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SOURCE_DIR = BASE_DIR / "src"


def inspect_path(path: Path) -> None:
    """Display common properties of a path."""
    print(f"Resolved: {path.resolve()}")
    print(f"Exists: {path.exists()}")
    print(f"Directory: {path.is_dir()}")
    print(f"File: {path.is_file()}")
    print(f"Name: {path.name}")
    print(f"Stem: {path.stem}")
    print(f"Suffix: {path.suffix}")
    print(f"Parent: {path.parent}")


def create_demo_structure() -> Path:
    """Create a temporary directory tree with several input files."""
    demo_dir = SOURCE_DIR / "pathlib_demo"
    nested_dir = demo_dir / "nested" / "monthly"
    nested_dir.mkdir(parents=True, exist_ok=True)
    (demo_dir / "orders.txt").write_text("ORD-001,paid\nORD-002,pending\n", encoding="utf-8")
    (demo_dir / "customers.txt").write_text("CUS-001,Ana\nCUS-002,Luis\n", encoding="utf-8")
    (nested_dir / "orders-2026-09.txt").write_text(
        "ORD-003,paid\n", encoding="utf-8"
    )
    (demo_dir / "ignored.csv").write_text("id,status\n1,paid\n", encoding="utf-8")
    return demo_dir


def process_text_files(demo_dir: Path) -> None:
    """Process direct text files with glob and nested files with rglob."""
    direct_files = sorted(demo_dir.glob("*.txt"))
    all_text_files = sorted(demo_dir.rglob("*.txt"))
    print(f"Direct text files: {[file.name for file in direct_files]}")
    print(f"All text files: {[file.name for file in all_text_files]}")
    for file_path in all_text_files:
        content = file_path.read_text(encoding="utf-8").strip()
        print(f"{file_path.relative_to(demo_dir)}: {content}")


def cleanup_demo_structure(demo_dir: Path) -> None:
    """Remove demo files first, then their empty directories."""
    for file_path in sorted(demo_dir.rglob("*")):
        if file_path.is_file():
            file_path.unlink()
    for directory in sorted(
        (path for path in demo_dir.rglob("*") if path.is_dir()),
        reverse=True,
    ):
        directory.rmdir()
    demo_dir.rmdir()


def main() -> None:
    """Demonstrate pathlib without leaving generated files behind."""
    inspect_path(SOURCE_DIR / "info.json")
    demo_dir = create_demo_structure()
    try:
        process_text_files(demo_dir)
    finally:
        cleanup_demo_structure(demo_dir)
        print(f"Demo directory removed: {not demo_dir.exists()}")


if __name__ == "__main__":
    main()