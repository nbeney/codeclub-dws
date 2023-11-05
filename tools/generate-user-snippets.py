"""
Utility script to generate user snippets for VS Code for our custom HTML elements.
The output can be loaed using File / Preferences / Configure User Snippets.
"""


# TODO: Extract the tags from the custom-elements/*.js files instead of hardcoding them here.
def get_tags():
    return [
        "cc-badge-easy",
        "cc-badge-hard",
        "cc-badge-medium",
        "cc-gz-app",
        "cc-gz-box",
        "cc-gz-buttongroup",
        "cc-gz-checkbox",
        "cc-gz-combo",
        "cc-gz-drawing",
        "cc-gz-listbox",
        "cc-gz-menubar",
        "cc-gz-picture",
        "cc-gz-pushbutton",
        "cc-gz-slider",
        "cc-gz-text",
        "cc-gz-textbox",
        "cc-gz-titlebox",
        "cc-gz-waffle",
        "cc-gz-window",
        "cc-library",
        "cc-navbar",
        "cc-project-card",
        "cc-project-filters",
        "cc-topic-card",
    ]


# Place your snippets for html here. Each snippet is defined under a snippet name and has a prefix, body and
# description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
# $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the
# same ids are connected.
# Example:
# "Print to console": {
# 	"prefix": "log",
# 	"body": [
# 		"console.log('$1');",
# 		"$2"
# 	],
# 	"description": "Log output to console"
# }
def print_snippet(key, prefix, body, description):
    print(
        f"""
"{key}": {{
    "prefix": "{prefix}",
    "body": [
        "{body}",
    ],
    "description": "{description}"
}},
""".strip()
    )


def handle_cc_badge(tag):
    if not tag.startswith("cc-badge-"):
        return
    body = f"<{tag}/>"
    print_snippet(tag, tag, body, tag)


def handle_cc_gz(tag):
    if not tag.startswith("cc-gz-"):
        return
    body = f"<{tag}/>"
    print_snippet(tag, tag, body, tag)


def handle_cc_library(tag):
    if not tag.startswith("cc-library"):
        return
    body = f'<cc-library name=\\"$1\\" description=\\"$2\\">$0</cc-library>'
    print_snippet(tag, tag, body, tag)


def handle_cc_navbar(tag):
    if not tag.startswith("cc-navbar"):
        return
    body = f'<cc-navbar active=\\"$1\\" level=\\"$2\\" />$0'
    print_snippet(tag, tag, body, tag)


def handle_cc_project_card(tag):
    if not tag.startswith("cc-project-card"):
        return
    body = f'<cc-project-card title=\\"$1\\" difficulty=\\"$2\\" path=\\"$3\\"></cc-project-card>$0'
    print_snippet(tag + " (internal)", tag + "-int", body, tag + " (internal)")
    body = f'<cc-project-card title=\\"$1\\" difficulty=\\"$2\\" href=\\"$3\\" img-src=\\"$4\\"></cc-project-card>$0'
    print_snippet(tag + " (external)", tag + "-ext", body, tag + " (external)")


def handle_cc_project_filters(tag):
    if not tag.startswith("cc-project-filters"):
        return
    body = f"<{tag}/>"
    print_snippet(tag, tag, body, tag)


def handle_cc_topic_card(tag):
    if not tag.startswith("cc-topic-card"):
        return
    body = f'<cc-topic-card path=\\"$1\\" title=\\"$2\\">$0</cc-topic-card>'
    print_snippet(tag, tag, body, tag)


if __name__ == "__main__":
    handle_cc_funcs = [v for k, v in globals().items() if k.startswith("handle_cc_")]

    for tag in get_tags():
        for func in handle_cc_funcs:
            func(tag)
