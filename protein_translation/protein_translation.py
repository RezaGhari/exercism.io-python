from textwrap import wrap
codon = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',	
    'UGG': 'Tryptophan',
}
def proteins(strand):
    splited = wrap(strand, 3)
    translated = list()
    for code in splited:
        if code in codon: translated.append(codon[code])
        else: break
    return translated