target = int(input("son kirit:"))
massiv = [5, 3, 3, 5, 7, 4, 4, 4]

def find_occurrences(massiv, target):
    occurrence_count = 0

    for num in massiv:
        if num == target:
            occurrence_count += 1

    return occurrence_count


print(find_occurrences(massiv, target))