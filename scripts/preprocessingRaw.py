from Bio import SeqIO 

seq = SeqIO.parse("/home/rudlab/projects/ferritinL.plantarumAn/data/ferritinL.plantarum.raw.fasta","fasta") 
seq_set = set() 
with open("/home/rudlab/projects/ferritinL.plantarumAn/data/ferritinL.plantarum.fasta", "w") as handle:
    for s in seq:
        if "ferritin" not in s.description:
            continue 
        if "X" in s.seq:
            continue
        if "partial" in s.description or "truncated" in s.description:
            continue 
        if s.seq not in seq_set:
            seq_set.add(s.seq) 
            SeqIO.write(s, handle, "fasta") 

