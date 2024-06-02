"""
Utility script to generate the ZIP archives for each activity.

There are 3 types of archives:
- resources.zip: contains only the resources (eg images, data files, etc)
- solution.zip: contains the resources and the full code 
- starter-kit.zip: contains the resources and the code template

The code template is the same as the full code, but with the student's code removed and replaced with a TODO comment.
"""

import shutil
import zipfile as zf
from pathlib import Path
from enum import Enum


class Mode(Enum):
    KEEP = 1
    STRIP = 2
    SANITIZE = 3


START_MARKER = "# CC:>>>>>"
STOP_MARKER = "# CC:<<<<<"


def filter_python_file(source_file, mode):
    result = []
    with open(source_file, "r") as f:
        ignore = False
        for line in f:
            line = line.rstrip()
            match mode:
                case Mode.KEEP:
                    result.append(line)
                case Mode.STRIP:
                    if not (
                        line.strip().startswith(START_MARKER)
                        or line.strip().startswith(STOP_MARKER)
                    ):
                        result.append(line)
                case Mode.SANITIZE:
                    if line.strip().startswith(START_MARKER):
                        indent = " " * (len(line) - len(line.lstrip()))
                        if indent:
                            result.append(f"{indent}pass  # TODO: ADD YOUR CODE HERE")
                        else:
                            result.append(f"# TODO: ADD YOUR CODE HERE")
                        ignore = True
                    elif line.strip().startswith(STOP_MARKER):
                        ignore = False
                    elif not ignore:
                        result.append(line)
    return "\n".join(result) + "\n"


def zipdir(source_dir, ziph, archive_dir, mode):
    for source_file in source_dir.glob("**/*"):
        if source_file.is_file() and "__pycache__" not in source_file.parts:
            archive_file = Path(
                archive_dir, *(source_file.parts[len(source_dir.parts) :])
            )
            if source_file.suffix == ".py":
                ziph.writestr(str(archive_file), filter_python_file(source_file, mode))
            else:
                ziph.write(source_file, arcname=archive_file)


def ziptoc(zip_file):
    with zf.ZipFile(zip_file, "r") as ziph:
        for info in ziph.infolist():
            print(info.filename)


def create_resources_archives():
    for resources_dir in Path("./activities").glob("**/solution/resources"):
        section_name = resources_dir.parts[1]
        activity_name = resources_dir.parts[2]
        zip_file = Path("./activities", section_name, activity_name, "resources.zip")
        print("GENERATE:", resources_dir, "===>", zip_file)
        zip_file.parent.mkdir(parents=True, exist_ok=True)
        with zf.ZipFile(zip_file, "w", zf.ZIP_DEFLATED) as ziph:
            zipdir(
                resources_dir, ziph, Path(activity_name, "resources"), mode=Mode.KEEP
            )
        # ziptoc(zip_file)
        # break


def create_solution_archives():
    for solution_dir in Path("./activities").glob("**/solution"):
        section_name = solution_dir.parts[1]
        activity_name = solution_dir.parts[2]
        zip_file = Path("./activities", section_name, activity_name, "solution.zip")
        print("GENERATE:", solution_dir, "===>", zip_file)
        zip_file.parent.mkdir(parents=True, exist_ok=True)
        with zf.ZipFile(zip_file, "w", zf.ZIP_DEFLATED) as ziph:
            zipdir(solution_dir, ziph, Path(activity_name), mode=Mode.STRIP)
        # ziptoc(zip_file)
        # break


def create_starterkit_archives():
    for solution_dir in Path("./activities").glob("**/solution"):
        section_name = solution_dir.parts[1]
        activity_name = solution_dir.parts[2]
        zip_file = Path("./activities", section_name, activity_name, "starter-kit.zip")
        print("GENERATE:", solution_dir, "===>", zip_file)
        zip_file.parent.mkdir(parents=True, exist_ok=True)
        with zf.ZipFile(zip_file, "w", zf.ZIP_DEFLATED) as ziph:
            zipdir(solution_dir, ziph, Path(activity_name), mode=Mode.SANITIZE)
        # ziptoc(zip_file)
        # break


def create_master_archive():
    master_file = Path("activity-packs.zip")
    master_file.parent.mkdir(parents=True, exist_ok=True)
    with zf.ZipFile(master_file, "w", zf.ZIP_DEFLATED) as ziph:
        for src_archive in Path("./activities").glob("**/*.zip"):
            section_name = src_archive.parts[1]
            activity_name = src_archive.parts[2]
            dst_archive = Path(
                "activity-packs", section_name, activity_name + "-" + src_archive.name
            )
            print("COLLECT:", src_archive, " ===> ", master_file, "as", dst_archive)
            ziph.write(src_archive, arcname=dst_archive)
    # ziptoc(master_file)


if __name__ == "__main__":
    create_resources_archives()
    create_solution_archives()
    create_starterkit_archives()
    create_master_archive()
