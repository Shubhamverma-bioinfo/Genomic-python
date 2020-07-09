#!/user/bin/python

def gc(dna):
    "this finction computes the gc % of a dna sequence"
    nbases=dna.count('n')+dna.count('N')
    gcbases=dna.count('g')+dna.count('c')+dna.count('G')+dna.count('C')
    gc_per=gcbases*100/(len(dna)-nbases)
    return print('gc percentage in the dna seq is %5.2f ' %gc_per)
    
# to find stop codon ['TAG','TGA','TAA']
def stop_codon_find(dna):
    dna=dna.upper()
    for i in range(0,len(dna),3):
        codon=dna[i:i+3]
        if codon in ['TAG','TGA','TAA']:
            break
    return print('dna seq has stop codon %s' %codon)