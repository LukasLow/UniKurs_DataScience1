
import matplotlib.pyplot as plt

# def ASSIGNMENT(new_list, i, old_list, j):
    # wird nicht benötigt
    # Funktionen werden grundsätzlich klein geschrieben
#     new_list[i] = old_list[j]


def merge_sort(list_to_sort_by_merge):
    # aus mergeSort wird merge_sort
    ## Überprüfen, ob die Liste mehr als ein Element enthält
    if (
        len(list_to_sort_by_merge) > 1
        # and not len(list_to_sort_by_merge) < 1
        # and len(list_to_sort_by_merge) != 0    beide zeilen sind unnötig
    ):
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        ## Rekursiver Aufruf von merge_sort für die linke und rechte Hälfte der Liste
        merge_sort(left)
        merge_sort(right)

        ## Initialisierung der Indizes
        l = 0
        r = 0
        i = 0

        ## Vergleiche und Zusammenführen der sortierten Hälften
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                # hier wird nicht mehr die ASSIGNMENT-Funktion verwendet
                ## Füge das kleinere Element aus der linken Hälfte in die resultierende Liste ein
                list_to_sort[i] = left[l]
                l += 1
            else:
                # hier wird nicht mehr die ASSIGNMENT-Funktion verwendet
                ## Füge das kleinere Element aus der rechten Hälfte in die resultierende Liste ein
                list_to_sort[i] = right[r]
                r += 1
            i += 1

        ## Füge die restlichen Elemente aus der linken Hälfte hinzu
        while l < len(left):
            # hier wird nicht mehr die ASSIGNMENT-Funktion verwendet
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        ## Füge die restlichen Elemente aus der rechten Hälfte hinzu
        while r < len(right):
            # hier wird nicht mehr die ASSIGNMENT-Funktion verwendet
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1

# Leerzeilen für bessere Übersichtlichkeit
## Eingangsliste
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

## Plot der Eingangsliste
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()

## Aufruf der merge_sort Funktion, um die Liste zu sortieren
merge_sort(my_list)

## Plot der sortierten Liste
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
