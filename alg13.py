

def WypiszPodzbiory(list):
    if len(list) == 0:
        return [[]]

    wynik = []
    for podzbior in WypiszPodzbiory(list[:-1]):
        podzbior2 = podzbior[:]
        podzbior2.append(list[-1])

        print(podzbior2)

        wynik.append(podzbior)
        wynik.append(podzbior2)

    return wynik


WypiszPodzbiory([1,2,3,4])