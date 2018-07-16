def transcribe(sequence):
    for ch in seq:
        rna_seq = seq.replace('T', 'U')
        return(rna_seq)

def translate_dna(sequence):
    codon2aa = {"AAA":"K", "AAC":"N", "AAG":"K", "AAU":"N", 
                "ACA":"T", "ACC":"T", "ACG":"T", "ACU":"T", 
                "AGA":"R", "AGC":"S", "AGG":"R", "AGU":"S", 
                "AUA":"I", "AUC":"I", "AUG":"M", "AUU":"I", 

                "CAA":"Q", "CAC":"H", "CAG":"Q", "CAU":"H", 
                "CCA":"P", "CCC":"P", "CCG":"P", "CCU":"P", 
                "CGA":"R", "CGC":"R", "CGG":"R", "CGU":"R", 
                "CUA":"L", "CUC":"L", "CUG":"L", "CUU":"L", 

                "GAA":"E", "GAC":"D", "GAG":"E", "GAU":"D", 
                "GCA":"A", "GCC":"A", "GCG":"A", "GCU":"A", 
                "GGA":"G", "GGC":"G", "GGG":"G", "GGU":"G", 
                "GUA":"V", "GUC":"V", "GUG":"V", "GUU":"V", 

                "UAA":"_", "UAC":"Y", "UAG":"_", "UAU":"T", 
                "UCA":"S", "UCC":"S", "UCG":"S", "UCU":"S", 
                "UGA":"_", "UGC":"C", "UGG":"W", "UGU":"C", 
                "UUA":"L", "UUC":"F", "UUG":"L", "UUU":"F"}

    ##the find method will give you the first index position (int) of the codon you're referring to 
    start_codon = sequence.find('ATG')

    ##You create a string of the starting nucleotide (A in this case) and rest of the sequence 
    seq_start = sequence[int(start_codon):]
    ##This selects the first nucleotide in codon/starting with with zero, selects for multiples of 3; n are multiples of 3 starting with 0
    for n in (0, len(seq_start), 3):
        if seq_start[n:n+3] in codon2aa:
            protein_seq += codon2aa[seq_start[n:n+3]]
    return protein_seq


seq = ''
with open('dna.fasta.py') as f_in:
    for line in f_in.readlines():
        if line[0] == '>':
            seq += (line.strip('>') + '     ')      
        else:
            transcribe(line)
            translate_dna(line)
            seq += (line)
print(seq)
