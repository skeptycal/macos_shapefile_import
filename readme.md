# Reading a shapefile from BASH environment using Python

It looks like you are using `macOS` or `Linux`, _so I will proceed with that assumption_.

## Test Environment Setup

_(You did not mention which OS version, IDE type, editor type, python version, python environment, virtual environtment, whether you are using jupyter, or any eccentric personalizations.)_

This is what I am using for these tests: macOS 10.14.4, VSCode Code 1.33.1, Python 3.7.3, CLI, VirtualEnv 16.4.3, pipenv version 2018.11.26, and shapefile version: 2.1.0

As of now, the latest commit to [GitHub](https://github.com/GeospatialPython/pyshp/commit/71231ddc5aa54f155d4f0563c56006fffbfc84e7) is: `Latest commit 71231dd on Feb 15`.

According to the [documentation](https://github.com/GeospatialPython/pyshp#overview), `Pyshp` is compatible with `Python 2.7-3.x`. It is very unlikely you have a Python version earlier than `2.7.x`, but to be thorough, we have to check. Look for output similar to this ...

```bash
$ python -VV

Python 3.7.3 (default, Mar 27 2019, 09:23:15)
[Clang 10.0.1 (clang-1001.0.46.3)]
```

_If this version is between 2.7.x and 3.6.x, you can be fairly certain that this is not the cause of problems._

---

# Troubleshooting the Type of Problem

Import problems can be due to problems with file location, path information, python path issues, code punctuation, file corruption, type definitions, os configuration, and probably a lot of other things that I don't even know about.

We need to narrow the problem down to the system level first. Is it a problem with the python environment? Is it using symlinks in the operating system? Is the path to our program or imported modules different than we thought it was?

Those are all good questions. I prefer to spend the least amount of time troubleshooting, so I try to plan my activities biased towards quick and simple actions.

### **I am checking in this order:**

**1. File location and path:** First, we want to know if this is a problem with the file location or path. This is easy to test and eliminates all of the more complicated problems.
**2. File condition and contents:** If the path isn't the problem, we check the files for problems. This is a bit harder to test, but very easy to solve.

3. If those are ok, then we get into the code. This may be the most complicated

### File Location and Path

- **Are the files actually there?** Change to the directory where the script is and make sure it matches what you are putting in the python file. This is in case there are odd home directories. Do you share this computer? Are you logged in under another user's account? Strange things happen ...

> You would very likely know all of this already, but I am just being complete.

```bash
$ echo $HOME
/Users/<username>/Documents

$ pwd
/path/to/file

$ whoami
<username>
```

> If anything here looks out of place or misspelled, fix it in the python file and try again.

- **Are the permissions correct?** List the permissions:

```bash
$ ls shapefile.*
-rw-r--r-- 1 <username> admin 87623 Apr 14 22:32 shapefile.dbf
-rw-r--r-- 1 <username> admin   143 Apr 14 22:32 shapefile.prj
-rw-r--r-- 1 <username> admin  2508 Apr 14 22:32 shapefile.shp
-rw-r--r-- 1 <username> admin   788 Apr 14 22:32 shapefile.shx
```

> If the owner should be you, but for some reason isn't, use this:

    `$ sudo chown whoami: staff shapefile.*`

> If the permissions should be readable by anyone, etc. modify that with:

    `$ sudo chmod 755 shapefile.*`

> If everything looks fine, continue onward ...

- **Is the program looking in the right place?** As a temporary test, copy (not move) the files into the same directory as the python script. The three files are `shapefile.shp`, `shapefile.shx`, and `shapefile.dbf` for these tests.

  `*` note (1) about the files required at the end of this post.

```bash
cp /path/to/file/shapefile.* .
```

> Remove the path info in the python file (temporarily) like this:

```python
# read the shapefile
#   (original code)
#   reader = shapefile.Reader('/Users/name/Documents/shapefile.shp')
reader = shapefile.Reader('shapefile.shp')
```

### File condition and contents

- **Are the files actually readable?** You are already using an absolute path, instead of a relative one, so that eliminates one problem. We see the files are there and have the correct permissions, but are they readable? Perhaps they have become corrupted? Perhaps they did not download correctly? Is the file readable from the OS? From another location? Try this:

_(The output may look like gibberish. If there is output with no errors, it is working.)_

```bash

$ cd ~/
$ head -n 5 /path/to/file/shapefile.shp
'
���j��rQS��b�cbC@��V��5S��XQ�Y�C@
l��\CHS�a��OfC@
����JS��b�cbC@
JqC@AS�d�'

$ cd /path/to/file
$ head -n 5 shapefile.shp
'
���j��rQS��b�cbC@��V��5S��XQ�Y�C@
l��\CHS�a��OfC@
����JS��b�cbC@
JqC@AS�d�'

$ head shapefile.shx
'
���j��rQS��b�cbC@��V��5S��XQ�Y�C@2
@
N
\'

$ head -c 500 shapefile.dbf | tr -d '[:blank:]'
'VanDornStreet#0000ffC�marker-symC�lineC�'

```

> At this point, we are fairly confident that the files are there and they are readable ... maybe the program just isn't looking in the right place?

---

## Python problems

### Problems using VSCode with virtual environments

> FYI, I have run into problems where the VSCode IDE (and pylint) reports that a module is not found but the program runs fine. It is some problem with the IDE and linter configuration but it does not affect the normal operation of the program, only IDE functions, debugging, etc.

> It seems to be an ongoing problem and I haven't tracked it down enough since it doesn't prevent me from running the programs. More information is found here:

- [VSCode Import Error for Python](https://stackoverflow.com/questions/46520127/vscode-import-error-for-python-module)
- [GitHub Issue](https://github.com/Microsoft/vscode/issues/10391)

### Solutions

> What I have done to get python modules to load in VSCode (when they do not at first) is to follow these steps:

- Before opening VSCode, create a virtual environment in the root folder of the project. I use pipenv to control both pip and venv together. I like it. I tend to also make this folder a GIT Repo and initialize NPM and any other utilities in this same root folder. Here are my suggestions (with #Comments) for a new project:

```bash
# Verify the directory I am in:
pwd
/Users/username/path/to/parent/

# Create new project directory and change to that directory
$ mkdir my-project && cd $_
mkdir: created directory 'my-project'

# Create GIT repo
$ git init
Initialized empty Git repository in /Users/username/path/to/parent/my-project/.git

# Create GitHub repo online from this GIT repo
$ hub create
Updating origin
https://github.com/username/my-project

# Initialize pipenv
$ pipenv --python 3.6.7
Creating a virtualenv for this project…
Pipfile: /Users/username/path/to/parent/my-project/Pipfile
Using /usr/local/bin/python3 (3.6.7) to create virtualenv…
⠼ Creating virtual environment...Using base prefix '/Library/Frameworks/Python.framework/Versions/3.6'
New python executable in /Users/username/.virtualenvs/my-project-L9l-38zD/bin/python3
Also creating executable in /Users/username/.virtualenvs/my-project-L9l-38zD/bin/python
Installing setuptools, pip, wheel...
done.
Running virtualenv with interpreter /usr/local/bin/python3

✔ Successfully created virtual environment!
Virtualenv location: /Users/username/.virtualenvs/my-project-L9l-38zD
Creating a Pipfile for this project…

# Activate Virtual Environment
$ pipenv shell
Launching subshell in virtual environment…
 . /Volumes/Data/skeptycal/.virtualenvs/my-project-L9l-38zD/bin/activate

~/Documents/now/projects/documentation/test/my-project
❯  . /Volumes/Data/skeptycal/.virtualenvs/my-project-L9l-38zD/bin/activate
```

> There are also a large number of things that can go wrong with python module importing due to the long history of the language and a desire of the maintainers to keep changes non-breaking. If all else fails, you may be running up against these python legacy issues. Here is a great overview:

- [Traps for the Unwary in Python’s Import System](http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html)

---

- If the program actually won't run because the module will not import, it is good to find out why. It may be a general import error, a typing issue, an os error, or something else.
- I have created a short test file to catch and report errors just to be sure. The repo is located here.
- The test program will
- If I am trying to import a module that is not installed, I get this error: `("No module named 'shapefile'",)`

---

`*` note (1)

According to the documentation for the Reader class:

- if one of the three files is missing, you will not find out until you attempt to use that file. So this is probably not the issue, but we can check ...
- We could start the reader without specifying a file, to test the import and reader, and `load()` the file afterwards. This seems like a last resort. There are no issues listed on GitHub related to these errors.
-

```py
class Reader(object):

"""
Reads the three files of a shapefile as a unit or
separately.  If one of the three files (.shp, .shx,
.dbf) is missing no exception is thrown until you try
to call a method that depends on that particular file.
The .shx index file is used if available for efficiency
but is not required to read the geometry from the .shp
file. The "shapefile" argument in the constructor is the
name of the file you want to open.

You can instantiate a Reader without specifying a shapefile
and then specify one later with the load() method.

Only the shapefile headers are read upon loading. Content
within each file is only accessed when required and as
efficiently as possible. Shapefiles are usually not large
but they can be.
"""
```
