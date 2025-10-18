from data_loader.data_loader import get_data_from_file
from task1.salary_analyzer import total_salary
from task2.cats_analyzer import get_cats_info

def main():
    # Task 1 start
    salary_data = get_data_from_file('task1/salary_data.txt')
    total, average = total_salary(salary_data)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    # Task 1 end

    print('\n')
    
     # Task 2 start
    cats_data = get_data_from_file('task2/cats_info.txt')
    cats_infromation = get_cats_info(cats_data)
    print(cats_infromation)
    # Task 2 end

if (__name__ == '__main__'):
    main()
