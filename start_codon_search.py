def read_fasta(filepath):
    """Reads a FASTA file and returns the DNA sequence as a string (no line breaks, no header)."""
    with open(filepath, 'r') as f:
        lines = f.readlines()
    # Remove header (starting with ">") and join the rest
    sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
    return sequence.upper()


def find_start_codons(dna_seq):
    """Find all positions of the 'ATG' start codon in a DNA sequence."""
    start_codon = "ATG"
    positions = []

    for i in range(len(dna_seq) - 2):
        codon = dna_seq[i:i+3]
        if codon == start_codon:
            positions.append(i)

    return positions


import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 start_codon_search.py <fasta_file>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    dna_sequence = read_fasta(fasta_file)
    start_positions = find_start_codons(dna_sequence)

    for pos in start_positions:
        frame = pos % 3
        print(f"ATG found at position {pos} (Frame {frame})")
