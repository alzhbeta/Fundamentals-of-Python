# ЛАБОРАТОРНАЯ РАБОТА №2 РАБОТА С ФАЙЛАМИ В PYTHON
# Вариант 1. Вычисление GC-состава
import os
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

def solve_variant_1(fasta_path: str) -> str:
    if not os.path.exists(fasta_path):
        raise FileNotFoundError(f"Файл не найден: {fasta_path}")
    best_id = 0
    max_gc = -1.0
    for record in SeqIO.parse(fasta_path, "fasta"):
        gc_now = gc_fraction(record.seq) * 100
        if gc_now > max_gc:
            max_gc = gc_now
            best_id = record.id
    return f"{best_id}\n{max_gc}"

if __name__ == "__main__":
    print(solve_variant_1("tests/input_1.txt"))
