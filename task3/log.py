from colorama import Fore

def print_file(name, level):
    indent = "    " * level 
    print(f"{indent}{Fore.YELLOW} {name}")

def print_directory(name, level):
    indent = "    " * level 
    print(f"{indent}{Fore.BLUE} {name}/")