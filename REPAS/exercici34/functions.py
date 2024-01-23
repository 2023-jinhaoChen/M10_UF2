def quadrat(num):
    return num*num

def my_map(my_fun, list):
    new_list = []
    for item in list:
        new_list.append(my_fun(item))
    return new_list