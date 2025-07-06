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
```
## Example output:
```
Start codons found at positions: [3, 10, 18, 26, 34]
```

## How it works

- The script reads the input FASTA file, strips out the header, and concatenates all lines into one continuous DNA sequence string.

- It then scans through the sequence to identify all "ATG" codons and records their starting positions.

## License
This project is open-source and available under the MIT License.
