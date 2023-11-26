import random
import math

def max_(my_list):
    position = 0
    max_value = my_list[position]
    for i, value in enumerate(my_list):
        if (value > max_value):
            max_value = value
            position = i
    return position, max_value

def min_(my_list):
    position = 0
    min_value = my_list[position]
    for i, value in enumerate(my_list):
        if (value < min_value):
            min_value = value
            position = i
    return position, min_value

def task1():
    print('Task 1:')
    my_list = []
    for i in range(10):
        my_list.append(random.randint(-10, 10))

    print(my_list)

    print(f'Max: {max(my_list)}')
    print(f'Min: {min(my_list)}')

    max_position, max_value = max_(my_list)
    print(f'My max found at: {max_position}, and the value is: {max_value}')
   
    min_position, min_value = min_(my_list)
    print(f'My min found at: {min_position}, and the value is: {min_value}')

    sum = 0
    for value in my_list:
        sum += value
    print(f'Sum: {sum}')
    average = sum / len(my_list)
    print(f'Average: {average}')

    lower_than_average = 0
    higher_than_average = 0
    for value in my_list:
        if value < average:
            lower_than_average += 1
        elif value > average:
            higher_than_average += 1
    print(f'Lower than average: {lower_than_average}')
    print(f'Higher than average: {higher_than_average}')

    print(f'List in correct order {my_list}')
    print(f'List in reverse order {my_list[::-1]}')

def task2():
    print('\n\nTask 2:')
    my_list = []
    for i in range(20):
        my_list.append(random.randint(1, 10))
    print(my_list)

    occurrences = {}
    for value in my_list:
        if value in occurrences:
            occurrences[value] += 1
        else:
            occurrences[value] = 1
    sorted_occurrences = dict(sorted(occurrences.items()))
    print(f'Sorted occurrences:{sorted_occurrences}')

def task3():
    print('\n\nTask 3:')
    my_list = []
    for i in range(5):
        inner_list = []
        for i in range(5):
            inner_list.append(random.randint(-5, 5))
        my_list.append(inner_list)

    print(f'Matrix (a list of lists):')
    for inner_list in my_list:
        for inner_element in inner_list:
            print(f'{inner_element:3}', end='')
        print()
    
    table_of_min_max = []
    for collumn_id in range(len(my_list)):
        collumn = []
        for row_id in range(len(my_list)):
            collumn.append(my_list[row_id][collumn_id])
        min_id, min_value = min_(collumn)
        max_id, max_value = max_(collumn)
        table_of_min_max.append([min_value, max_value])
    
    for i, inner_list in enumerate(table_of_min_max):
        print(f'Collumn #{i} min: {inner_list[0]} max: {inner_list[1]}')

def task4():
    print('\n\nTask 4:')
    a = int(input('Enter start: '))
    b = int(input('Enter end: '))
    my_list = []
    for i in range(a, b + 1):
        if i % 2 == 1:
            my_list.append(i)
    print(my_list)
    for i in range(len(my_list)):
        variable = my_list[i]
        my_list[i] = (variable, math.pow(2, variable), math.sqrt(variable))
    print(my_list)

def task5():
    print('\n\nTask 5:')
    start = int(input('Enter start: '))
    end = int(input('Enter end: '))
    n = int(input('Enter n: '))
    my_list = []
    for i in range(n):
        inner_list = []
        for j in range(n):
            inner_list.append(random.randint(start, end))
        my_list.append(inner_list)
    for inner_list in my_list:
        for inner_element in inner_list:
            print(f'{inner_element:3}', end='')
        print()

    sum_of_diagonal = 0
    for i in range(len(my_list)):
        sum_of_diagonal += my_list[i][i]
    print(f'Sum of diagonal (left to right): {sum_of_diagonal}')
    
    sum_of_diagonal = 0
    for i in range(len(my_list)):
        sum_of_diagonal += my_list[i][len(my_list)-i-1]
    print(f'Sum of diagonal (right to left): {sum_of_diagonal}')

    sum_of_numbers_on_odd_positions = 0
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            if (    ((i+1) % 2 == 1)
                and ((j+1) % 2 == 1)):
                sum_of_numbers_on_odd_positions += my_list[i][j]
                print(f"Odd position: {i+1} x {j+1}")
    print(f'Sum of numbers on odd positions: {sum_of_numbers_on_odd_positions}')

    for i in range(len(my_list)):
        my_list[i] = my_list[i][::-1]
    my_list = my_list[::-1]
    print(f'Reversed matrix:')
    for inner_list in my_list:
        for inner_element in inner_list:
            print(f'{inner_element:3}', end='')
        print()

def task6():
    print('\n\nTask 6:')
    size = int(input('Enter size: '))
    my_list = []
    for i in range(size):
        inner_list = []
        for j in range(size):
            sign = "+"
            for k in range(2, min(i+1, j+1) + 1):
                if (    ((i+1) % k == 0)
                    and ((j+1) % k == 0)):
                    sign = "-"
                    break
            inner_list.append(sign)
        my_list.append(inner_list)
    
    print(f'Matrix:')
    for inner_list in my_list:
        for inner_element in inner_list:
            print(f'{inner_element:3}', end='')
        print()

def main():
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()

if __name__ == '__main__':
    main()