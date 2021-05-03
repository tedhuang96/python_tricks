import pathhack
from src.folder_0.file_0 import func_sum
from src.folder_1.file_1 import func_sum_product

def main():
    a, b, c, d = 1., 2., 3., 4.
    print(func_sum(a, b)) # 3
    print(func_sum(c, d)) # 7
    print(func_sum_product(a, b, c, d)) # 21

if __name__ == '__main__':
    main()