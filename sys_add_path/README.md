# sys_add_path
This is a trick to show how to use sys.path.append() to help python files in different subfolders to import each other.

## Run the code
```
python sys_add_path/scripts/main.py
```
or
```
cd sys_add_path && python scripts/main.py
```
or <br/>
```
cd sys_add_path/scripts && python main.py
```

#### Note that you don't have to go to the folder in order to make sure package path is recognized.


## The code format
```
import sys
import os
from os.path import abspath, join, split
file_path = split(abspath(__file__))[0]
pkg_path = join(file_path, relative_project_folder_path) # project folder
sys.path.append(pkg_path)
```
relative_project_folder_path may be changed according to the python file's path.