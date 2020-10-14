import sys
from os.path import abspath, join, split
file_path = split(abspath(__file__))[0]
# If you comment add pkg_path in a source file, when you try to run
# the debug on functions like below, you will get an error.
# However, if you have added pkg_path in your script, say main.py, then
# here adding pkg_path in src file is not necessary.
pkg_path = join(file_path, '../..') # project folder
sys.path.append(pkg_path)

from src.utils import boo

def model_func(b):
    b = b + 10
    boo(b)

if __name__ == "__main__":
    model_func(10)
