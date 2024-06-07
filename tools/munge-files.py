"""
Utility script to modify HTML files.
"""

import os
from pathlib import Path

import regex


def get_html_files():
    return sorted(list(Path(".").glob("**/*.html")))


def insert_line_before(html_file, line, new_line):
    # Convert line to regex
    re = regex.compile(line)

    with open(html_file, "r") as file:
        lines = file.readlines()

    for i, l in enumerate(lines):
        # if re.match(l.strip()) is not None:
        if '/style.css' in l.strip():
            lines.insert(i, new_line + "\n")
            break

    with open(html_file, "w") as file:
        file.write("".join(lines))


if __name__ == "__main__":
    for html_file in get_html_files():
        if html_file.parts[0] == "offline":
            continue

        print(f"Processing {html_file}")
        # insert_line_before(html_file, "</body>", "    <cc-copyright></cc-copyright>")
        insert_line_before(html_file, '/style.css"', '    <script src="/custom-elements/custom-copyright.js"></script>')
