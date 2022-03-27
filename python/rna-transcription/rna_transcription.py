def to_rna(dna_strand):
    rna = ""
    for char in dna_strand:
        if char == "G":
            rna = f"{rna}C"
        if char == "C":
            rna = f"{rna}G"
        if char == "T":
            rna = f"{rna}A"
        if char == "A":
            rna = f"{rna}U"
    return rna

