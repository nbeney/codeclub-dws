# codeclub-dws

## Introduction

This page and repository proposes a simple process for downloading Python packages to be used by the CodeClub students.

The process is:
1. The CodeClub organizers maintain a list of Python packages they want to use.
2. The IT Team downloads the packages in the list (script provided).
3. The IT Team reviews the downloaded packages (security checks, content, etc).
4. The IT Team installs the downloaded packages into a location (eg local folder or network drive) accessible by all the CodeClub students.

The process is incremental and can easily be run each time the list of Python packages is modified.

## Details

### [requirements.txt](requirements.txt)

Contains the list of the Python packages to download from [PyPI](https://pypi.org) (Python Package Index). 

For example:

```
adventurelib
colorama
emoticon
fastapi
flask
guizero
mediapipe
networkzero
pandas
pgzero
printy
pyfiglet
pyttsx3
sympy
z3-solver
```

It is possible to specify a version (exact, minimum, etc) for each package but we do not need this for now. 

### [download.bat](download.bat) / [download.sh](download.sh)

Reads `requirements.txt` and downloads all the packages (including their dependencies) into `./python-packages/` (created automatically). 

Uses `pip` which should be included in any recent Python distribution.

```bash
pip install --requirement=./requirements.txt --target=./python-packages --upgrade
```

Rerunning the script will upgrade the existing packages and download the additional ones.
  
### python-packages/

Contains the downloaded Python packages as specified in `requirements.txt` (including their dependencies). Managed by `download.bat`/`download.sh`.

```bash
$ tree ./python-packages -d -L 1
./python-packages
├── Flask-2.3.2.dist-info
├── Jinja2-3.1.2.dist-info
├── MarkupSafe-2.1.3.dist-info
├── PIL
├── Pillow-10.0.0.dist-info
...
├── tzdata-2023.3.dist-info
├── werkzeug
├── z3
├── z3_solver-4.12.2.0.dist-info
└── zmq

122 directories
```

This folder must be accessible (read-only) by all the students attending CodeClub. This could be through:

1. **local copy** on each PC in the IT room where CodeClub is held
2. **network drive** accessible from each PC in the IT room where CodeClub is held

A priori #2 should be easier to manage.

### [codeclub_dws.py](codeclub_dws.py)

A convenience Python file that adds the location of `python-packages/` to `PYTHONPATH` which is the list of 
folders where a Python program can import packages from.

```python
import sys

# Path to the folder (local or network) containing the Python packages.
PATH_TO_PYTHON_PACKAGES = TBD  # TODO: eg "c:\\CodeClub\\python-packages" or "\\\\CodeClub\\python-packages"

sys.path.append(PATH_TO_PYTHON_PACKAGES)
```

The students would copy this file into their project folder and import it into their main program (see hereunder for an example).

### [demo-adventurelib.py](demo-adventurelib.py)

A Python demo program that uses some downloaded Python packages. 

```python
# Add ".../CodeClub/python-packages/" to PYTHONPATH.
import codeclub_dws

# Import the required downloaded packages.
from adventurelib import *
from printy import inputy
from pyfiglet import print_figlet

...
```
