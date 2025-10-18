from pathlib import Path

def get_data_from_file(path):
    base_dir = Path(__file__).parent.parent
    file_path = base_dir / path    

    try:
        with open(file_path, 'r', encoding='UTF-8') as file:
            try:
                return [el.strip() for el in file.readlines()]
            except:
                print('Something is wrong, please check file data')
                return []
    except:
        print('File not found')
        return []
        