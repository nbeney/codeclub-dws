import os
import zipfile as zf
from pathlib import Path


def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            path = Path(root, file)
            arc = Path("resources", file)
            ziph.write(path, arcname=arc)


if __name__ == "__main__":
    for solution_dir in Path("./activities").glob("**/solution"):
        zip_file = solution_dir.parent.joinpath("resources.zip")
        resources_dir = solution_dir.joinpath("resources")
        print(resources_dir, "===>", zip_file)
        with zf.ZipFile(zip_file, "w", zf.ZIP_DEFLATED) as ziph:
            zipdir(resources_dir, ziph)
