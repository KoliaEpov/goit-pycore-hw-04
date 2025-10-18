def get_cats_info(list):
    cats = []
    for cat_info_string in list:
        cat_info = cat_info_string.split(',')
        cats.append({'id': cat_info[0], 'name': cat_info[1], 'age': cat_info[2]})
    
    return cats