from pathlib import Path

def total_salary(path: str):
    salary_list = get_data_from_file(path)
    salary_information = []
    for user_information in salary_list:
        try:
            salary_information.append(float(user_information.split(',')[1]))
        except:
            print('salary is missing')
    
    return (sum_salary(salary_information), mid_salary(salary_information))

def sum_salary(list):
    sum = 0 
    for item in list:
        sum += item

    return sum

def mid_salary(list):
    if (list):
        return sum_salary(list) / len(list)
    else:
        return 0


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
    total, average = total_salary('salary_data.txt')
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if (__name__ == '__main__'):
    main()
