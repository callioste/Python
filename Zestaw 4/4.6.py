# Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać
# zagnieżdżone podsekwencje. Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest
# sekwencją, wykonać przez isinstance(item, (list, tuple)).

def sum_seq(sequence):
    sum = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            sum += sum_seq(item)
        else:
            sum += item
    return sum

sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]

assert sum_seq(sequence) == 45