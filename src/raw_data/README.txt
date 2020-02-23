=== sub-challenge 2  ===
train_cli.tsv: this file contains clinical information (gender and msi status) for the 80 training samples. 
train_pro.tsv: proteomics data based on spectral counting. Each row represents a protein and each column represents a training sample. 
train_rna.tsv: RNA-seq data based on FPKM reads. Each row represents a gene and each column represents a training sample.
sum_tab_2.csv: real labels for the training samples. Each row represents the real labels of the three data sources for the corresponding training sample. E.g. for Training_2, both the clinical and RNA-seq data are from Training_2 while the proteomics data are actually from Training_80.
test_cli.tsv:  this file contains clinical information (gender and msi status) for the 80 testing samples. 
test_pro.tsv:  similar to train_pro.txt, but for testing samples.
test_rna.tsv:  similar to train_rna, but for testing samples.
