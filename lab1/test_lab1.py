import pytest
from lab1 import (
    calculate_rabbits, mortal_rabbits, hamming_dist, 
    gene_permutations, k_mers, oriented_permutations, 
    mendel_law, expected_offspring
)

# Вариант 1. Кролики
@pytest.mark.parametrize("n, k, expected", [
    (5, 3, 19), (6, 3, 40), (5, 5, 41), (12, 1, 144), 
    (20, 2, 349525), (33, 2, 2863311531)
])
def test_v1(n, k, expected):
    assert calculate_rabbits(n, k) == expected

# Вариант 2. Смертные кролики
@pytest.mark.parametrize("n, m, expected", [
    (12, 15, 144), (6, 3, 4), (33, 2, 1), (33, 1, 0),
    (100, 3, 1177482265857), (4, 10, 3), (4, 5, 3),
    (18, 12, 2556), (20, 14, 6737), (10, 3, 12), (9, 4, 19)
])
def test_v2(n, m, expected):
    assert mortal_rabbits(n, m) == expected

# Вариант 3. Дистанция Хэмминга
def test_v3():
    s = "GAGCCTACTAACGGGAT"
    t = "CATCGTAATGACGGCCT"
    assert hamming_dist(s, t) == 7

# Вариант 4. Перестановки
def test_v4():
    count, perms = gene_permutations(3)
    assert count == 6
    expected_perms = [(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)]
    for p in expected_perms:
        assert p in perms

# Вариант 5. k-меры
def test_v5():
    letters = ["A", "C", "G", "T"]
    res = k_mers(letters, 2)
    assert len(res) == 16
    expected = ["AA", "AC", "AG", "AT", "CA", "CC", "CG", "CT", "GA", "GC", "GG", "GT", "TA", "TC", "TG", "TT"]
    for item in expected:
        assert item in res

# Вариант 6. Ориентированные перестановки
def test_v6():
    count, perms = oriented_permutations(2)
    assert count == 8
    expected = [(-1,-2), (-1,2), (1,-2), (1,2), (-2,-1), (-2,1), (2,-1), (2,1)]
    for p in expected:
        assert p in perms

# Вариант 7. Мендель
@pytest.mark.parametrize("k, m, n, expected", [
    (2, 2, 2, 0.783333), (3, 3, 3, 0.770833), (1, 1, 1, 0.8333),
    (0, 5, 5, 0.4444), (10, 0, 0, 1.0), (5, 5, 0, 0.9444),
    (0, 3, 3, 0.45), (20, 23, 15, 0.79386), (1, 1, 0, 1.0),
    (27, 30, 28, 0.746008), (26, 26, 25, 0.75863)
])
def test_v7(k, m, n, expected):
    assert mendel_law(k, m, n) == pytest.approx(expected, abs=1e-4)

# Вариант 8. Потомство
@pytest.mark.parametrize("counts, expected", [
    ([1, 0, 0, 1, 0, 1], 3.5),
    ([1, 2, 3, 4, 5, 6], 23.0),
    ([0, 0, 0, 10, 10, 10], 25.0),
    ([1, 2, 2, 2, 2, 2], 15.0),
    ([10, 0, 0, 0, 0, 0], 20.0),
    ([0, 10, 0, 0, 0, 0], 20.0)
])
def test_v8(counts, expected):
    assert expected_offspring(counts) == expected
