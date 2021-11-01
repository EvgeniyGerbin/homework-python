stud_list = {
    "Nikita Konev": [3, 5, 5, 3, 4],
    "Herbin Evgeniy": [4, 5, 5, 5, 5],
    "Maksim Meleshko": [2, 2, 2, 2, 2],
    "Dima Kytsenko": [4, 4, 5, 4, 5],
    "Sasha Samoilov": [5, 4, 3, 3, 5],
    "Lisa Boroh": [5, 5, 5, 5, 5]
}

def mean(lst):
    return sum(lst) / len(lst)

sortedIds = sorted(list(stud_list.keys()), key=lambda studentId: mean(stud_list[studentId]))

print('The best student:', sortedIds[-1])
print('Worst student:', sortedIds[0])