from lab4.modules.fetch_sequences import get_records
from lab4.modules.analyze_gc import sort_by_gc
from lab4.modules.translate_sequences import extract_and_translate

def main():
    records = get_records()
    
    print("\n=== ЗАДАНИЕ 2: GC-СОСТАВ (СОРТИРОВКА) ===")
    sorted_gc = sort_by_gc(records)
    for gc_val, r in sorted_gc:
        print(f"{r.id}: {r.description}, GC = {gc_val:.6f}")
        
    print("\n=== ЗАДАНИЕ 3: ТРАНСЛЯЦИЯ CDS ===")
    translations = extract_and_translate(records)
    for item in translations:
        print(f"{item['id']}: {item['desc']}")
        print(f"Coding sequence location = {item['location']}({item['strand']})")
        print("Translation =")
        print(item['translation'])
        print("-" * 30)

if __name__ == "__main__":
    main()

