# Bioinformatics-problems
# Transcribing DNA to RNA
![image](https://user-images.githubusercontent.com/66241504/150932757-dd4e409c-8eca-43c5-a3d6-8d461268b7ed.png)
- G --> C
- C --> G
- A --> U
- T --> U

# Transalting RNA to protein
It is the process in which the genetic code in mRNA is read, one codon at a time, to make a protein. After mRNA leaves the nucleus, it moves to a ribosome, which consists of rRNA and proteins. The ribosome reads the sequence of codons in mRNA. Molecules of tRNA bring amino acids to the ribosome in the correct sequence.
- DNA strings: formed over the alphabet {A, C, G, T} to model single strands of DNA (the opposing strand can be inferred by taking the string's reverse complement);
- RNA strings: formed over the alphabet {A, C, G, U} to model strands of RNA;
- Protein strings: formed over a 20-symbol alphabet containing all the letters of the English alphabet except for B, J, O, U, X, and Z. Used to model the polypeptide chains that make up much larger protein structures.
- The genetic code for RNA (also called as codon table) shows how we uniquely relate a 4-nucleotide sequence [A, U, G, C] to a set of 20 amino acids.
![image](https://user-images.githubusercontent.com/66241504/150935851-c11b9bd7-8032-4fe2-9c8e-6eb68a23e3b2.png)
- First step is to split your rna sequence into groups of 3 (triplets)
- Secondly, use the genetic code table  to read which amino acid corresponds to the current codon. The first circle starting from the center represents the first character of the codon, the second circle represents the second character and the third circle represents the last character. After translating, you will receive a protein sequence which corresponds to the aforementioned RNA sequence.
- Finally, UAA, UAG and UGA are termination points, meaning, the translation process needs to be stopped when it encounters these points.
