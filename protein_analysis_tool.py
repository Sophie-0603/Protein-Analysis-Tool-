

############################################################################
#Protein Analysis Tool. 
#Can provide Mw, amino acid composition, molar extinction coefficient, charged residue composition, overall estimated protein charge and hydropathicity score from a FASTA sequence file. 

#########################################

#Count Aminos
#Go through sequence as a string and count each time there is a residue. If the residue type has been previously counted, add 1 to the dictionary. If it has not been counted yet, assign 1 to the value. Create a dictionary with the residue as the key and the number of times it occured as the value. 

from colorama import init, Fore, Back, Style

init()
from sys import stdout

def amino_acid_count(sequence):
    count = {}
    for amino in sequence:
        keys = count.keys()
        if amino in keys:
            count[amino] += 1
        else:
            count[amino] = 1
    return count

###################################################

#Calculate molar extinction coeff

#Take the number of times either W, or C are present in the sequence and * by the respective amino acid molar extinction coefficient i.e. W = 5500, Y = 1490
#Cysteine in disulphide bonds has an extinction coeff of 125, but reduced cysteine has a negligible absorbance at 280nm. 
def molar_extinction_coeff(sequence):
    from colorama import Fore, Back, Style 
    print(Style.BRIGHT + "Molar Extinction Coefficient")
    amino_count = amino_acid_count(sequence)
    reduced = amino_count["Y"]*1490 + amino_count["W"]*5500
    oxidised= reduced + (amino_count["C"]//2)*125
     
    print(Fore.RED + "Predicted molar extinction coeffiencts (M-1 cm-1) at 280nm are:")
    print(Style.RESET_ALL)
    print("Reduced form:", reduced)
    print("Oxidised form:", oxidised)
    print()

################################################    
#Presents the amino acid count in a table with the percentage of each amino acid. Done by converting the dictionary into a dataframe using pandas. Then added an extra column to calculate the percentage amino acid. Had issues trying to add the percentage column to the dataframe but found similar code online to do this through df['x']= code. 
 
    
def amino_acid_count_output(sequence):
    from colorama import Fore, Back, Style 
    import pandas as pd
    print(Style.BRIGHT + "Amino Acid Composition", Style.RESET_ALL)
    count_dict = amino_acid_count(sequence)
  
    key_values = count_dict.items()
    new_d = {str(key):int(value) for key, value in key_values}
    df = pd.DataFrame(new_d.items(), columns=["Amino Acid", "Count"])
   
    df['Percent composition (%)'] = (df['Count'] / df['Count'].sum() * 100)
    print(df)
    print()
    
#####################################################    
    
#Calculate the molecular weight of the supplied sequence using a dictionary of each amino acid's molecular weights. Had issues getting correct molecular weight as did not account for water molecules lost during condensation reactions, so incorporated this later by multiplying the molecular weight of water by the length of the sequence and subtracting this from the total. 
    
Mw_amino_acid = {

'G':75.1, 'A':89.1, 'V':117.1, 'L':131.2, 'I':131.2, 'M':149.2, 'P':115.1, 'F':165.2, 'W':204.2, 'N':132.1, 'Q':146.2, 'S':105.1, 'T':119.1, 'Y':181.2, 'C':121.2, 'D':133.1, 'E':147.1, 'K':146.2, 'R':174.2, 'H':155.2

}




def molecular_weight(aa_sequence):
    from colorama import Fore, Back, Style 
    print(Style.BRIGHT + "Molecular Weight", Style.RESET_ALL)
    Mw = 0
    for amino_acid in aa_sequence:
    
        Mw_output = Mw_amino_acid[amino_acid]
        Mw += Mw_output
    #need to take into account water molecules lost during condensation
    water_molecules_excluded = 18.01528 * len(aa_sequence)
    Mw = Mw - water_molecules_excluded
    Mw_in_kDa = Mw / 1000
 
    print(Fore.RED + "The Molecular Weight is:", Style.RESET_ALL, Mw, "Da", "/", Mw_in_kDa, "kDa")
    print()

   
 ###################################################
 #Estimated net protein charge. Created a dictionary with the the charge of each charged residue as the value and the residue name as the key. Additively add the charges together for every charged residue that appears in the sequence. 


def protein_charge(aa_sequence):
    
    from colorama import Fore, Back, Style 
    print(Style.BRIGHT + "Estimated Protein Charge", Style.RESET_ALL)


    Residue_charge = {"C":-.045,"D":-.999, "E":-.998,"H":.091,"K":1,"R":1,"Y":-.001}
    charge = 0
    for amino in aa_sequence:
        if amino in Residue_charge:
            charge += Residue_charge[amino]
    print(Fore.RED + "Estimated protein charge:", Style.RESET_ALL, charge)
    print()
    
#####################################################

#Count the number of positively and negatively charged residues in a sequence. Provided a list of either positively or negatively charged residues and created a loop to run through the sequence and every time one of the listed residues is counted 1 is added to the count.     
def negative_amino_counter(aa_sequence):
    
    from colorama import Fore, Back, Style
  

    negative_aas = ( "D", "E")


    count = 0
    for amino in aa_sequence:
        if amino in negative_aas:
            count += 1
            
    print(Fore.RED + "Number of negatively charged amino acids (Asp and Glu):", Style.RESET_ALL, count)
    
    print()
    
    
def positive_amino_counter(aa_sequence):
    from colorama import Fore, Back, Style 
    print(Style.BRIGHT + "Charged Residue Composition", Style.RESET_ALL)
    positive_aas = ("K", "R")
    
    count = 0
    for amino in aa_sequence:
        if amino in positive_aas:
            count += 1
            
    print(Fore.RED + "Number of positively charged amino acids (Arg and Lys):", Style.RESET_ALL, count)
    

###################################################    
    
#Created a function to calculate the hydropathicity score for the protein. Created a dictionary containing the hydropathicity score for each amino acid taken from Kyte and Doolittle, 1982. Similarly to the charge calculation, averaged the total hydropathicity scores for each residue in the sequence to give final score. 

hydropathicity_scale = {'A': 1.800, 'C':2.500, 'D':-3.500, 'E': -3.500, 'F':2.800, 'G':-0.400, 'H':-3.200, 'I':4.500, 'K':-3.900, 'L':3.800, 'M':1.900, 'N':-3.500, 'P':-1.600, 'Q':-3.500, 'R':-4.500, 'S':-0.800, 'T':-0.700, 'V':4.200, 'W':-0.900, 'Y':-1.300}    
    
def hydropathicity_score(sequence):
    print(Style.BRIGHT + "Hydropathicity Score", Style.RESET_ALL)
    print()
    
    score = 0 
    
    for amino_acid in sequence:
        hydropathicity_output = hydropathicity_scale[amino_acid]
        score += hydropathicity_output
        
    hydropathicity_score = score/ len(sequence)
    
    print(Fore.RED + "Hydropathicity score is derived using individual amino acid scores supplied by Kyte and Doolittle, 1982. A more positive score indicates hydrophobicity and a more negative score indicates hydrophilicity", Style.RESET_ALL)
    
    print()
        
    print("Score:", hydropathicity_score)
    
##########################################################

#Final Protein analysis tool. Combined all the other functions into one function so a list of information about the supplied protein will be the output. Ideally wanted to insert this output into a .txt file but could not work out how to do this, so stuck with terminal output. 
    
def protein_analysis(sequence):
    
    
    molecular_weight(sequence)

    amino_acid_count_output(sequence)

    molar_extinction_coeff(sequence)

    protein_charge(sequence)
    
    positive_amino_counter(sequence)
    
    negative_amino_counter(sequence)
    
    hydropathicity_score(sequence)
            
        
        
    
   
   
        
   
    