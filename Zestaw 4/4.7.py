# Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości.
# Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji. Wskazówka: rozważyć wersję rekurencyjną,
# a sprawdzanie czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

def flatten(sequence):
    newL = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            newL.extend(flatten(item))

        else:
            newL.append(item)

    return newL

sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(sequence))
