##############################################################################
##  Introduction to DNA Translation
##
"""
   * For a long time, it was not clear what molecules were able to copy and 
     transmit genetic information.
     - We now know that this information is carried by the dioxyribonucleic 
       acid or DNA in all living things.
       
   * DNA is a discrete code physically present in almost every cell of an 
     organism.
     - We can think of DNA as a one dimensional string of characters with 
       four characters (A,C,G,T) to choose from.
       
   * Each unique three character sequence of nucleotides, sometimes called 
     a nucleotide triplet, corresponds to one amino acid.
     - The sequence of amino acids is unique for each type of protein and 
       all proteins are built from the same set of just 20 amino acids for 
       all living things.
       
   * The central dogma of molecular biology that describes the basic flow 
     of genetic information:
     - DNA -> RNA -> Protein

   * What we want to do?
     - DNA --> amino acid
     
   * In this case study, we have four tasks.
     1. The first task is to manually download DNA and protein sequence data 
        to your computer.
     2. The second task is to import the DNA data into Python.
     3. The third task is to create an algorithm that translates to DNA using 
        the translation table we will provide.
     4. The fourth task, the final task, is to check if your DNA translation 
        matches the protein string you have downloaded.
"""
#-----------------------------------------------------------------------------

##############################################################################
##  Download DNA Data
##
"""
   * The NCBI is the National Center for Biotechnology Information, and it is 
     United States' main public repository of DNA and related information.
     
   * We will download two files from the NCBI.
     - The first is a strand of DNA. ("dna.txt")
     - The second is the corresponding protein sequence of amino acids 
       translated from this DNA. ("protein.txt")
           
"""
#-----------------------------------------------------------------------------

##############################################################################
##  Importing DNA Data Into Python
##
"""
   * The best way to read a file depends on what you want to do with the file.
     - If you need to read a large file, but you're only interested in some 
       of the lines, not all of them, you could read the file in a for loop, 
       one line at a time, process the line, or skip it, and move onto the 
       next line.
     - Another option is to read the entire file in one go.
     
   * Before you start working with files, make sure that your Python 
     working directory corresponds to the directory where you downloaded 
     your files.

"""
#-----------------------------------------------------------------------------


# remove extra characters




##############################################################################
##  Translating the DNA Sequence
##
"""
   * The translation process is essentially a table lookup operation.
     - Use dictionary as the lookup table.
     - The table is "table.py"
     - Copy the table dictionary in the file.

"""
#-----------------------------------------------------------------------------



table = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}







##############################################################################
##  Comparing Your Translation
##
"""
   * Compare your translation to the official one obtained from the NCBI
     website.

"""
#-----------------------------------------------------------------------------


# CDS: 21:938





