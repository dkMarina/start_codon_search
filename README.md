# Start Codon Search

This Python script searches for all occurrences of the start codon **ATG** in a DNA sequence from a FASTA file.

## Features

- Reads DNA sequences from FASTA files (ignores headers and line breaks)  
- Finds all positions where the "ATG" start codon appears  
- Prints the list of positions with their respective reading frames (0, 1, or 2)

## Requirements

- Python 3.x (no additional packages required)

## Usage

Run the script from the command line:

```bash
python3 start_codon_search.py path/to/your/sequence.fasta
