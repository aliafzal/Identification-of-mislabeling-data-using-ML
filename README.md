ML-mislabel-identification

# Detecting Mislabeled Genomics Data using Machine Learning Models

## Contents
#### Data and Analysis
1. The genomics raw data in csv format and its analysis with a readme file are in the [src folder](https://github.com/hpazooki/ML-mislabel-identification/tree/master/src). The libraries used are: pandas & numpy for handling the data, scikit-learn & scipy for analysis, and matplotlib & seaborn for visualizations
2. Prints of the code ported to Scala for AWS EMR Spark cluster and its results are in the [spark folder](https://github.com/hpazooki/ML-mislabel-identification/tree/master/spark). The rationale behind it is explained in more detail in the final report.

#### Results
The written research paper is in the [docs folder](https://github.com/zpazooki/ML-mislabel-identification/tree/master/docs). The quantitative results are included in the code notebooks. 

## Summary
For the final research project in the EE542: Cloud Computing course, my team members and I chose to participate in a data science challege proposed by PrecisionFDA, a cloud-based DNA sequencing data platform developed by the Food and Drug Administration. 

The challenge's objective was to explore various methods of detecting human error in data collection, which is currently a critical roadblock that can occur in quatitative clinical research. The provided datasets were extremely limited by design and the training set was identical in size to the test dataset provided. The challenge was to use a small training set of correctly labeled samples to train a model that is able to detect future errors in a similiar context. For a more detailed explanation, see the challenge proposal blurb in Nature magazine [(/docs/mislabeling_correction_challenge.pdf)](https://github.com/hpazooki/ML-mislabel-identification/blob/master/docs/mislabeling_correction_challenge.pdf). The summary figure is attached below
![alt text](https://github.com/zpazooki/ML-mislabel-identification/blob/master/img/1.png) 


The provided data for the 80 training samples were of two types: genomics data and their correposnding metadata about gender and tumor msi type. The Proteomics and RNA-seq data were extremely wide each consisting of hundreds of columns for each of the 80 samples, 20,000 total attributes for each, which is characteristic of genomics data in general. 

In summary, our approach was to use the provided information in the correctly labeled samples to map each of the two metadata to the proteomics and rna data, and then use that information to identify samples with mislabeled metadata. For example, if according to our model the proteomics data indicates that the patient is male but she is labeled as a female, the sample would be flagged as mislabeled. Our method is laid out in more detail in our research paper [(/docs/report.pdf)](https://github.com/hpazooki/ML-mislabel-identification/blob/master/docs/report.pdf), with the technical summary in its appendix.

The abstract from our paper is attached below. I was responsible for sections II, III, and IV in the report.

<br>



</br>
          
![alt text](https://github.com/zpazooki/ML-mislabel-identification/blob/master/img/2.png)
