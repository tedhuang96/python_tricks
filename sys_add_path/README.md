# sys_add_path (will be fixed)
This is a trick to show how to use sys.path.append() to help python files in different subfolders to import each other.

## Run the code
```
python sys_add_path/scripts/main.py
```
or
```
cd sys_add_path && python scripts/main.py
```
or
```
cd sys_add_path/scripts && python main.py
```
Note that you don't have to go to the folder in order to make sure package path is recognized.


## The code format
```
import sys
from os.path import abspath, join, split
file_path = split(abspath(__file__))[0]
pkg_path = join(file_path, relative_project_folder_path) # project folder
sys.path.append(pkg_path)
```
relative_project_folder_path may be changed according to the python file's path.

## Notes
If you comment add pkg_path in a source file, when you try to run
the debug on functions in that src file, you will get an error. <br/>
However, if you have added pkg_path in your script, say main in scripts folder, then
it is not necessary to add pkg_path in src file. In the meantime, if you add pkg_path in src file, it does not harm anything.