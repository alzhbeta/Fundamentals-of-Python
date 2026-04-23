# ЛАБОРАТОРНАЯ РАБОТА №1
# ОСНОВНЫЕ ОПЕРАТОРЫ И КОНСТРУКЦИИ PYTHON

from math import factorial
from itertools import permutations, product

# Вариант 1. Кролики и рукуррентные отношения
def calculate_rabbits(n, k):
    last_month, this_month = 1, 1
    for _ in range(3, n + 1):
        last_month, this_month = this_month, this_month + k * last_month
    return this_month

# Вариант 2. Смертные кролики Фибоначчи
def mortal_rabbits(n, m):
    ages = [0] * m
    ages[0] = 1
    for month in range(1, n):
        newborns = sum(ages[1:])
        ages = [newborns] + ages[:-1]
    return sum(ages)

# Вариант 3. Подсчёт точечных мутаций
def hamming_dist(s, t):
    hamming_distance = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            hamming_distance += 1
    return hamming_distance

# Вариант 4. Перичисление последовательностей генов
def gene_permutations(n):
    count = factorial(n)
    perms = list(permutations(range(1, n + 1)))
    return count, perms

# Вариант 5. Лексикографическое перечисление k-меров
def k_mers(letters, n):
    return ["".join(combination) for combination in product(letters, repeat=n)]

# Вариант 6. Перечисление ориентированных генных последовательностей
def oriented_permutations(n):
    numbers = [x for i in range(1, n + 1) for x in (i, -i)]
    results = [p for p in permutations(numbers, n) if len(set(abs(x) for x in p)) == n]
    return len(results), results

# Вариант 7. Первый закон Менделя
def mendel_law(k, m, n):
    total = k + m + n
    probability = 1 - ((n * (n - 1)) + 0.25 * (m * (m - 1)) + m * n) / (total * (total - 1))
    return round(probability, 6)

# Вариант 8. Вычисление ожидаемого числа потомков
def expected_offspring(a):
    a1, a2, a3, a4, a5, a6 = a
    return 2 * a1 + 2 * a2 + 2 * a3 + 1.5 * a4 + 1 * a5 + 0 * a6

# БЛОК ЗАПУСКА
if __name__ == "__main__":
    # Вариант 1. Кролики и рукуррентные отношения
    n1, k1 = map(int, input("Введите номер месяца и количество пар кроликов в помёте: ").split())
    print(calculate_rabbits(n1, k1))

    # Вариант 2. Смертные кролики Фибоначчи
    n2, m2 = map(int, input("Введите количество месяцев и срок жизни кроликов: ").split())
    print(mortal_rabbits(n2, m2))

    # Вариант 3. Подсчёт точечных мутаций
    s3, t3 = input("Введите первую строку ДНК: "), input("Введите вторую строку ДНК: ")
    print(hamming_dist(s3, t3))

    # Вариант 4. Перичисление последовательностей генов
    n4 = int(input("Введите длину n перестановок: "))
    count4, perms4 = gene_permutations(n4)
    print(count4)
    for p in perms4: 
        print(*p)

    # Вариант 5. Лексикографическое перечисление k-меров
    let5 = input("Введите последовательность из максимум 10 символов, определяющих упорядоченный алфавит, через пробел: ").split()
    n5 = int(input("Введите натуральное число n <= 10: "))
    for res in k_mers(let5, n5): 
        print(res)

    # Вариант 6. Лексикографическое перечисление k-меров
    n6 = int(input("Введите длину n перестановок: "))
    count6, perms6 = oriented_permutations(n6)
    print(count6)
    for p in perms6: 
        print(*p)

    # Вариант 7. Первый закон Менделя
    k7, m7, n7 = map(int, input("Введите k, m, n: ").split())
    print(mendel_law(k7, m7, n7))

    # Вариант 8. Вычисление ожидаемого числа потомков
    a8 = list(map(int, input("Введите 6 целых неотрицательных чисел через пробел: ").split()))
    print(expected_offspring(a8))
