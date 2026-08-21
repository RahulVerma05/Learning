def proteins(strand):
    acid = []
    acid_dict = { "AUG"	: "Methionine",
                  "UUU"	: "Phenylalanine",
                  "UUC" : "Phenylalanine",
                  "UUG"	: "Leucine",
                  "UUA" : "Leucine",
                  "UCU" : "Serine",
                  "UCC" : "Serine",
                  "UCA" : "Serine",
                  "UCG" : "Serine",
                  "UAU" :	"Tyrosine",
                  "UAC" : "Tyrosine",
                  "UGU" :	"Cysteine",
                  "UGC" : "Cysteine",
                  "UGG"	: "Tryptophan",
    }
    strand_list =[]
    for i in range(0,len(strand),3):
        strand_list.append(strand[i:i+3])
    for rna in strand_list:
        if rna in acid_dict:
            acid.append(acid_dict[rna])
        else:
            break
    return acid
