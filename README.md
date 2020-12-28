# Protein-Analysis-Tool-
A tool that when provided with a target's protein sequence will provide biochemical information 

This is a tool written in Python that can take a protein sequence and feedback information about the encoded protein including:

-Molecular weight
-Amino acid composition 
-Molar extinction coefficients 
-Hydropathicity score
-Predicted protein charge
-Charged amino acid count

To run:

1. Download the two Python scripts 'protein_analysis_tool.py' and 'FASTA_file_open.py' in addition to a protein sequence in the FASTA file format (the BamA protein FASTA file is supplied but any FASTA file will be applicable, the BamA file name is 'bama.fasta'). Ensure all the files are in the same directory. The script 'protein_analysis_tool.py' is a module that contains functions that calculate the factors listed above (e.g molecular weight) where as 'FASTA_file_open.py' allows the user to insert the sequence FASTA file and import the required functions. 

2. In the FASTA_file_open.py script, add the name of the FASTA file after sequence_file (line 7). For example, sequence_file = "BamA.fasta" .

3. Run the script in the terminal and you will be given an output of information about the target protein. The first line of the FASTA file including protein information such as name is listed as the first line of output to avoid confusion if multiple proteins are analysed sequentially. This is then followed by information about the target protein separated by headings in bold. The data itself will be displayed in black text, where as extra information to understand the data will be displayed in red. 

Explanation of code: 

-Molecular weight:
This function uses a dictionary containing the molecular weight of each amino acid. It runs through the supplied sequence and adds  the corresponding molecular weight for each residue it encounters. It then substracts the weight of one water molecular per amino acid to account for the water lost during the condensation reaction during peptide formation. The resulting molecular weight is provided in both Da and kDa in the output. 

-Amino acid composition:
Within the amino_acid_count function, the protein sequence is read as a string and each time an amino acid is encoutered it is counted and put into a dictionary. If the residue has appeared previously, one will be added to the count. This dictionary was then converted into a dataframe using pandas and a percentage composition was calculated. This percentage composition was then added to the dataframe in the function amino_acid_count_output. 

-Molar Extinction Coefficient:
Within the molar extinction coefficient function, the amino_acid_count function is used again. The number of times Tyrosine, Tryptophan or Cystine (in the case of the oxidised extinction coefficient) appears in the sequence is extracted from the dictionary and multiplied by the respective individual amino acid extinction coefficient. 

-Estimated protein charge:
For this function, a dictionary containing the charged amino acids and their associated charge. The sequence is then read through in a loop and the charged associated with each residue that is encountered is added to the total 'count'. 

-Charged residue composition:
Two lists were created, one containing all the positively charged residues (Lys and Arg) and one containing the negatively charged residues (Asp and Glu). A loop was created in which the supplied sequence was read through and every time a positively or negatively charged residue is encountered, one is added to the count. 

-Hydropathicity score:
A hydropathicity score for each amino acid was taken from Kyte & Doolittle, 1982 and converted into a dictionary. The protein sequence was then looped through, and the hydropathicity score associated with each amino acid encountered was added to the total score. This total score was then divided by the length of the sequence to obtain an average hydropathicity score for the protein. The more positive the score the more hydrophobic the protein, the more negative the score the more hydrophilic the protein. 

