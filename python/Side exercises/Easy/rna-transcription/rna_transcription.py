def to_rna(dna_strand: str) -> str:
    translation = str.maketrans("GCTA", "CGAU")
    rna = str.translate(dna_strand, translation)
    return rna
