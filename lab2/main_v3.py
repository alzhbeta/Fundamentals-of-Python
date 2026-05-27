# ЛАБОРАТОРНАЯ РАБОТА №2 
# РАБОТА С ФАЙЛАМИ В PYTHON

# Вариант 3. Нахождение мРНК по протеину
from Bio.Data import CodonTable
from collections import defaultdict

def solve_variant_3(protein_seq: str) -> int:
    table = CodonTable.standard_rna_table
    
    codon_counts = defaultdict(int)
    for codon, aa in table.forward_table.items():
        codon_counts[aa] += 1
        
    stop_codons_count = len(table.stop_codons)
    
    combinations = stop_codons_count
    MOD = 1_000_000
    
    for aa in protein_seq:
        combinations = (combinations * codon_counts[aa]) % MOD
            
    return combinations

if __name__ == "__main__":
    print(solve_variant_3("MA"))

