def get_cats_info(path):
    list = get_data_from_file(path)
    cats = []
    for cat_info_string in list:
        cat_info = cat_info_string.split(',')
        cats.append({'id': cat_info[0], 'name': cat_info[1], 'age': cat_info[2]})
    
    return cats

def get_data_from_file(path):
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            try:
                return [el.strip() for el in file.readlines()]
            except:
                print('Something is wrong, please check file data')
                return []
    except:
        print('File not found')
        return []
    

def main():
    cats_infromation = get_cats_info('cats_info.txt')
    print(cats_infromation)

if (__name__ == '__main__'):
    main()
