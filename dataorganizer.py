import os
import shutil
import argparse
import logging
from typing import Dict, List

# Mapping extensions -> folders
CATEGORIES: Dict[str, List[str]] = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".wmv"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".ppt", ".pptx"],
    "Music": [".mp3", ".wav", ".flac", ".aac"],
    "Others": [],
}


def organize_files(base_folder: str) -> None:
    """
    Organize files into subfolders based on their extensions.

    Args:
        base_folder (str): The root folder where files will be organized.
    """
    logging.info("Starting organization from: %s", base_folder)

    for root_dir, _, files in os.walk(base_folder):
        for filename in files:
            source_path = os.path.join(root_dir, filename)
            _, extension = os.path.splitext(filename)
            extension = extension.lower()

            target_folder = "Others"
            for category, extensions in CATEGORIES.items():
                if extension in extensions:
                    target_folder = category
                    break

            final_dir = os.path.join(base_folder, target_folder)
            os.makedirs(final_dir, exist_ok=True)

            if os.path.normpath(root_dir) == os.path.normpath(final_dir):
                logging.debug("File '%s' is already in the correct folder.", filename)
                continue

            target_path = os.path.join(final_dir, filename)
            target_path = avoid_overwrite(target_path)

            try:
                shutil.move(source_path, target_path)
                logging.info("Moved: '%s' -> '%s'", filename, target_folder)
            except Exception as e:
                logging.error("Error moving '%s': %s", filename, e)


def avoid_overwrite(path: str) -> str:
    """
    Ensure that files are not overwritten if a file with the same name already exists.

    Args:
        path (str): Original target file path.

    Returns:
        str: A new unique path if conflict exists.
    """
    base, extension = os.path.splitext(path)
    counter = 1
    new_path = path

    while os.path.exists(new_path):
        new_path = f"{base}_{counter}{extension}"
        counter += 1

    return new_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="File organizer by category."
    )
    parser.add_argument(
        "folder", help="Path of the folder to be organized."
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Show detailed logs."
    )

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="[%(levelname)s] %(message)s",
    )

    organize_files(args.folder)


if __name__ == "__main__":
    main()
