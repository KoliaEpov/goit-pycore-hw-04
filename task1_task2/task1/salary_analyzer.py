def total_salary(salary_list):
    salary_information = []
    for user_information in salary_list:
        try:
            salary_information.append(int(user_information.split(',')[1]))
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