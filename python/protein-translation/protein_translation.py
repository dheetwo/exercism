# Globals for proteins
METHIONINE = {
    "AUG"
}

PHENYLALANINE = {
    "UUU",
    "UUC"
}

LEUCINE = {
    "UUA",
    "UUG"
}

SERINE = {
    "UCU",
    "UCC",
    "UCA",
    "UCG"
}

TYROSINE = {
    "UAU",
    "UAC"
}

CYSTEINE = {
    "UGU",
    "UGC"
}

TRYPTOPHAN = {
    "UGG"
}

STOP = {
    "UAA",
    "UAG",
    "UGA"
}

def proteins(strand):
    protein_list = []
    while len(strand) > 0:
        print(strand[:3])
        if strand[:3] in STOP:
            break
        elif strand[:3] in METHIONINE:
            protein_list.append("Methionine")
        elif strand[:3] in PHENYLALANINE:
            protein_list.append("Phenylalanine")
        elif strand[:3] in LEUCINE:
            protein_list.append("Leucine")
        elif strand[:3] in SERINE:
            protein_list.append("Serine")
        elif strand[:3] in TYROSINE:
            protein_list.append("Tyrosine")
        elif strand[:3] in CYSTEINE:
            protein_list.append("Cysteine")
        elif strand[:3] in TRYPTOPHAN:
            protein_list.append("Tryptophan")
        strand = strand[3:]
    return protein_list
