def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

d = {
     "Nikita Konev": [3, 5, 5, 3, 4],
     "Herbin Evgeniy": [4, 5, 5, 5, 5],
     "Maksim Meleshko": [2, 2, 2, 2, 2],
     "Dima Kytsenko": [4, 4, 5, 4, 5],
     "Sasha Samoilov": [5, 4, 3, 3, 5],
     "Lisa Boroh": [5, 5, 5, 5, 5]
     }
p = []
for key, val in d.items():
     val = mean(val)
     d = {key: val}
     sortedIds = sorted(list(d.keys()), key=lambda studentId: mean(d[studentId]))

     print('лучший:', sortedIds[-1])
     print('худший:', sortedIds[0])

