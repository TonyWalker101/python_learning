#small program to solve string replacement kata

def dna_to_rna(dna):
  if dna == "":
      return
  rna = dna.replace("T", "U")
  return rna