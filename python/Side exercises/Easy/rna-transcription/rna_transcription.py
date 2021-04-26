def to_rna(dna_strand):
    translation = str.maketrans("GCTA", "CGAU")
    rna = str.translate(dna_strand, translation)
    return rna
