def extract_and_translate(records):
    results = []
    for record in records:
        for feature in record.features:
            if feature.type == "CDS":
                location = feature.location
                strand = "+" if location.strand >= 0 else "-"
                cds_seq = feature.extract(record.seq)
                protein_seq = cds_seq.translate(to_stop=True)
                
                results.append({
                    "id": record.id,
                    "desc": record.description,
                    "location": f"[{location.start}:{location.end}]",
                    "strand": strand,
                    "translation": str(protein_seq)
                })
    return results

