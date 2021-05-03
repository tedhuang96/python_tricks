import sys
from os.path import abspath, join, split
# * Hack project path
file_path = split(abspath(__file__))[0]
pkg_path = join(file_path, '..')
sys.path.append(pkg_path)

# print(abspath(__file__))
# print(file_path)
# print(pkg_path)