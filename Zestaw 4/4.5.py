# Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru
# left do right włącznie. Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.

def odwracanie_iter(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    return L

def odwracanie_rek(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        return odwracanie_rek(L, left + 1, right - 1)
    return L

L1 = [1, 2, 3, 4, 5, 6, 7]

print(odwracanie_iter(L1, 2, 5))

L2 = [1, 2, 3, 4, 5, 6, 7]

print(odwracanie_rek(L2, 2, 5))