import sys
from pathlib import Path
from log import print_directory, print_file

def main():
    iterate_directory(sys.argv[1])
    
def iterate_directory(path, level=0):
    directory_path = Path(path)
    if (directory_path.exists()):
        for path in directory_path.iterdir():
            if (path.is_dir()):
                print_directory(path.name, level)
                iterate_directory(path, level+1)
            else:
                print_file(path.name, level)
    else:
        print('Directory not found')


if (__name__ == '__main__'):
    main()

