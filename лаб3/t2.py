# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def finding_common_participants(first, second, razdelka=','):
    first_ = first.split(razdelka)
    second_ = second.split(razdelka)
    first_set = set(first_)
    second_set = set(second_)
    intersection_set = first_set.intersection(second_set)
    intersection_list = list(intersection_set)
    intersection_list.sort()
    return intersection_list


commoners = finding_common_participants(participants_first_group, participants_second_group, '|')
print(commoners)

# TODO Провеьте работу функции с разделителем отличным от запятой
