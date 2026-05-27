from Bio.SeqUtils import gc_fraction

def sort_by_gc(records):
    sorted_records = []
    for r in records:
        gc_val = gc_fraction(r.seq)
        sorted_records.append((gc_val, r))
    sorted_records.sort(key=lambda x: x[0])
    return sorted_records
