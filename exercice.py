#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List
import math


def convert_to_absolute() -> float:
    a = float(input('Nombre: '))
    if a < 0 :
        a = -a
    return a


def use_prefixes() -> List[str]:
    prefixes, suffixes, output = 'JKLMNOP', 'ack', []
    for pre in prefixes :
        output.append(f'{pre}{suffixes}')
    return output


def prime_integer_summation() -> int:
    num, count, summation = 2, 0, 0
    while count < 100 :
        isPrime = True
        for i in range(2, int(math.sqrt(num)) + 1) :
            if(num % i == 0) : 
                isPrime = False
        if(isPrime) :
            summation += num
            count += 1
        num += 1
    return summation


def factorial(number: int) -> int:
    for i in range(1, number) :
        number *= i
    return number


def use_continue() -> None:
    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
