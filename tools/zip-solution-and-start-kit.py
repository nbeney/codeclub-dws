import os
import zipfile as zf


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        # print("root:", root)
        # print("dirs:", dirs)
        # print("files:", files)
        # print()
        for file in files:
            print("Add file:", os.path.join(root, file))
            ziph.write(os.path.join(root, file))


# with zf.ZipFile("./test.zip", "w", zf.ZIP_DEFLATED) as ziph:
#     zipdir("./activities/python-libraries", ziph)


def find_solution_dirs():
    for root, dirs, files in os.walk("./activities"):
        if root.endswith("\\solution"):
            yield root


if __name__ == "__main__":
    for dir_ in find_solution_dirs():
        print(dir_)
