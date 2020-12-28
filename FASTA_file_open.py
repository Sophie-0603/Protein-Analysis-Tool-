#Protein Analysis Tool!#

#Please insert the target protein's FASTA sequence file below. Please ensure the file is in the same directory as this script in addition to 'protein_analysis_tool.py'

sequence_file = "Insert FASTA file name here"

#importing FASTA file and using that as input sequence.  
#prevented the first info line from the FASTA file being read so only the sequence is being read. Removed the new space from each new line 

with open(sequence_file, "r") as sequence:
    content = sequence.readlines()[1:]
output = "".join(content)
dna = output.replace("\n", "")
sequence=dna

#Inserted this bit of code in case I needed to run sequence after sequence and didn't want the results to get mixed up. This takes the first line of the FASTA file (which will have info about the target protein i.e. name) and will insert this at the top of each new output. 




from colorama import init, Fore, Back, Style
init()
from sys import stdout
file = open(sequence_file)
line_number = 1
for i in range(line_number):
    line= file.readline()
print(Style.BRIGHT + line)


#importing the tool and using it on the supplied sequence 
import protein_analysis_tool
from colorama import Fore, Back, Style
protein_analysis_tool.protein_analysis(sequence)


