from lab4.modules.fetch_sequences import get_records
from lab4.modules.analyze_gc import sort_by_gc
from lab4.modules.translate_sequences import extract_and_translate

def main():
    records = get_records()

    sorted_gc = sort_by_gc(records)
    for gc_val, r in sorted_gc:
        print(f"{r.id} GC = {gc_val:.6f}")

    translations = extract_and_translate(records)
    for item in translations:
        print(f"{item['id']} {item['location']}({item['strand']})")
        print(item['translation'])


if __name__ == "__main__":
    main()

