#small program to solve string replacement kata

def dna_to_rna(dna):
  # if dna == "":
  #     return
  # rna = dna.replace("T", "U")
  # return rna
  return dna.replace("T", "U") if dna != "" else None

#tests

#should equal "UUUU"
print(dna_to_rna("TTTT"))
#should equal "GCAU"
print(dna_to_rna("GCAT"))
#should equal "GACCGCCGCC"
print(dna_to_rna("GACCGCCGCC"))