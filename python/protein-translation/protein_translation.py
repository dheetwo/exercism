from protein import protein_list, STOP


def proteins(strand):
    translation = []
    while len(strand) > 0:
        if strand[:3] in STOP:
            break
        for protein in protein_list:
            if protein[0].__contains__(strand[:3]):
                translation.append(protein[1])
        strand = strand[3:]
    return translation
