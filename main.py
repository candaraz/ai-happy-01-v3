"""Write the entry image to entry.png.

The repository holds the finished image as image.jpg. This program copies
those bytes, unchanged, to the output directory: /output in the grader's
container, or MAKEFUN_OUTPUT_DIR when set (the kit's local-test convention).
It uses only the standard library, needs no network, and produces the same
bytes on every run.
"""

import os
import shutil

IMAGE_NAME = "image.jpg"
OUTPUT_NAME = "entry.png"


def output_dir():
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return override if override else "/output"


def main():
    # realpath, not abspath: resolve symlinks so the image is found even if
    # the repository is reached through a symlinked path.
    here = os.path.dirname(os.path.realpath(__file__))
    source = os.path.join(here, IMAGE_NAME)
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(target_dir, OUTPUT_NAME))


if __name__ == "__main__":
    main()
