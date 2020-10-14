import sys
from os.path import abspath, join, split
file_path = split(abspath(__file__))[0]
pkg_path = join(file_path, '..') # project folder
sys.path.append(pkg_path)

from src.deep_src.model import model_func

if __name__ == "__main__":
    model_func(20)